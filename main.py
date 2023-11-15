from collections import deque
pilha = deque(['A', 'E', 'I', 'O'])
print(pilha) # Saída: ['A', 'E', 'I', 'O']
pilha.append('U') # Adicionar no topo da lista
print(pilha) # Saída: ['A', 'E', 'I', 'O', 'U']
pilha.pop() # Remover 'U' do topo da lista
pilha.pop() # Remover 'O' do topo da lista
pilha.pop() # Remover 'I' do topo da lista
pilha.pop() # Remover 'E' do topo da lista
pilha.pop() # Remover 'A' do topo da lista
