from sentence_transformers import SentenceTransformer, util
import json
import torch

# Carrega modelo leve e base de conhecimento
modelo = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')
with open('base_pandas.json', 'r', encoding='utf-8') as f:
    base = json.load(f)

# Pré-calcula embeddings da base
perguntas = [item['pergunta'] for item in base]
embeddings = modelo.encode(perguntas, convert_to_tensor=True)

print("\n=== CONSULTA PANDAS OFFLINE ===")
print("Digite sua dúvida ou 'sair' para encerrar.\n")

while True:
    pergunta = input(">>> ")
    if pergunta.lower() in ['sair', 'exit']:
        break

    emb_user = modelo.encode(pergunta, convert_to_tensor=True)
    # calcula similaridades e pega o vetor 1D
    scores = util.cos_sim(emb_user, embeddings)[0]  

    # pega os 3 maiores scores e seus índices
    topk = torch.topk(scores, k=3)  

    print("\nTop 3 respostas possíveis:")
    for idx, score in zip(topk.indices.tolist(), topk.values.tolist()):
        print(f"- {base[idx]['resposta']}  (score: {score:.2f})")

    # opcional: só retorna o melhor se for acima de um threshold
    if topk.values[0] >= 0.5:
        melhor = base[topk.indices[0]]["resposta"]
        print(f"\nResposta escolhida: {melhor}\n")
    else:
        print("\nNão encontrei resposta confiável. Tente reformular.\n")
