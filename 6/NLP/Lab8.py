import torch
import torch.nn as nn
import torch.optim as optim

data = [('hello', 'namaste'), ('thank you', 'dhanyavaad'), ('bye', 'alvida')]
def build_vocab(sentences):
	vocab = {'<pad>': 0, '<sos>': 1, '<eos>': 2}
	for s in sentences:
		for w in s.split():
			if w not in vocab:
				vocab[w] = len(vocab)
	return vocab

SRC = build_vocab([s for s, _ in data])
TGT = build_vocab([t for _, t in data])
IDX2TGT = {i: w for w, i in TGT.items()}

def tensorize(text, vocab):
	return torch.tensor([vocab['<sos>']] + \
		[vocab[w] for w in text.split()] + [vocab['<eos>']])

class Encoder(nn.Module):
	def __init__(self, input_dim, emb_dim, hid_dim):
		super().__init__()
		self.emb = nn.Embedding(input_dim, emb_dim)
		self.rnn = nn.GRU(emb_dim, hid_dim, batch_first=True)

	def forward(self, x):
		x = self.emb(x)
		return self.rnn(x)
	
class Attention(nn.Module):
	def __init__(self, hid_dim):
		super().__init__()
		self.attn = nn.Linear(hid_dim * 2, 1)

	def forward(self, hidden, enc_outs):
		hidden = hidden.permute(1, 0, 2).repeat(1, enc_outs.shape[1], 1)
		energy = torch.tanh(self.attn(torch.cat((hidden, enc_outs), dim=2)))
		weights = torch.softmax(energy.squeeze(2), dim=1)
		return weights

class Decoder(nn.Module):
	def __init__(self, output_dim, emb_dim, hid_dim, attention):
		super().__init__()
		self.emb = nn.Embedding(output_dim, emb_dim)
		self.rnn = nn.GRU(emb_dim + hid_dim, hid_dim, batch_first=True)
		self.fc = nn.Linear(hid_dim * 2, output_dim)
		self.attn = attention

	def forward(self, x, hidden, enc_outs):
		x = self.emb(x).unsqueeze(1)
		a = self.attn(hidden, enc_outs).unsqueeze(1)
		c = torch.bmm(a, enc_outs)
		rnn_input = torch.cat((x, c), dim=2)
		output, hidden = self.rnn(rnn_input, hidden)
		out = self.fc(torch.cat((output.squeeze(1), c.squeeze(1)), dim=1))
		return out, hidden

E = Encoder(len(SRC), 16, 32)
A = Attention(32)
D = Decoder(len(TGT), 16, 32, A)
optE = optim.Adam(E.parameters(), lr=1e-2)
optD = optim.Adam(D.parameters(), lr=1e-2)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(100):
	for src, tgt in data:
		se = tensorize(src, SRC).unsqueeze(0)
		te = tensorize(tgt, TGT)
		enc_out, hidden = E(se)
		loss = 0
		x = te[0]
		for i in range(1, len(te)):
			output, hidden = D(torch.tensor([x]), hidden, enc_out)
			loss += loss_fn(output, te[i].unsqueeze(0))
			x = te[i]
		optE.zero_grad()
		optD.zero_grad()
		loss.backward()
		optE.step()
		optD.step()

def translate(text):
	se = tensorize(text, SRC).unsqueeze(0)
	enc_out, hidden = E(se)
	
	x = torch.tensor([TGT['<sos>']])
	result = []
	for _ in range(10):
		o, hidden = D(x, hidden, enc_out)
		x = o.argmax(1)
		if x == TGT['<eos>']:
			break
		result.append(IDX2TGT[x.item()])
	return ' '.join(result)

print(translate('hello'), translate('thank you'))
