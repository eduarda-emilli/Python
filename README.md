<h1 style="text-align: center;">Python: Introdução</h1>
<span>Estou estudando Python pelo Curso em Vídeo e decidi compartilhar os exercícios que tenho feito até o momento. Já completei a maioria e estou determinada a concluir todos eles (são mais de cem). Em cada resolução, vou tentar explicar o processo por trás da solução e também vou deixar minhas anotações para futuras dúvidas, tanto para mim quanto para quem estiver lendo. Espero que essa iniciativa possa ser útil e contribuir de alguma forma!</span>
<hr>

<h2>Agora vamos ao que interessa... o que exatamente é o Python? 🤔</h2>
<span style="font-size: 15px">Resumindo é uma linguagem de programação de alto nível, interpretada e de propósito geral. Foi criada por Guido van Rossum e lançada pela primeira vez em 1991. Uma das principais características do Python é sua sintaxe simples e legibilidade, o que a torna uma ótima escolha para iniciantes na programação. Python é conhecida por sua filosofia de "baterias inclusas", o que significa que ela fornece uma vasta biblioteca padrão com uma ampla gama de módulos e funcionalidades prontos para uso. Isso facilita o desenvolvimento de uma variedade de aplicações, desde scripts simples até aplicativos complexos.</span>
<hr>

<h2>Conceitos básicos do Python</h2>

<table>
  <tr>
    <th>Conceito</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td><a href="#criando-variaveis">Variáveis</a></td>
    <td>Em Python, você pode atribuir valores a variáveis usando o sinal de igual (=).</td>
  </tr>
  <tr>
    <td><a href="#tipos-de-dados">Tipos de dados</a></td>
    <td>Python possui vários tipos de dados embutidos, como inteiros, ponto flutuante, strings, listas, tuplas, dicionários, etc.</td>
  </tr>
  <tr>
    <td><a href="#operadores">Operadores</a></td>
    <td>Python suporta operadores aritméticos e operadores de comparação para realizar operações matemáticas e comparações entre valores.</td>
  </tr>
  <tr>
    <td><a href="#estruturas-condicionais">Estruturas condicionais</a></td>
    <td>O Python utiliza a estrutura if-elif-else para executar diferentes blocos de código com base em condições específicas.</td>
  </tr>
  <tr>
    <td><a href="#estruturas-de-repeticao">Estruturas de repetição</a></td>
    <td>O Python oferece estruturas de repetição, como for e while, para executar um bloco de código várias vezes.</td>
  </tr>
</table>

<hr>

<h2>Tendo conhecimento da parte teórica do Python, vamos para um pouco de prática! 🥳</h2>

## Criando Variáveis

<a name="criando-variaveis"></a>

Nesta seção, vamos praticar como criar variáveis em Python. As variáveis são usadas para armazenar e representar valores em nosso código.

Para criar uma variável em Python, você precisa atribuir um valor a ela usando o sinal de igual (`=`). Veja um exemplo simples:

```python
# Criando uma variável chamada 'idade' e atribuindo o valor 25
idade = 25

# Imprimindo o valor da variável idade
print(idade)  # Saída: 25

# Realizando operações matemáticas com a variável idade
dobro_idade = idade * 2
print(dobro_idade)  # Saída: 50

# Concatenando a variável idade com uma string
mensagem = "Minha idade é: " + str(idade)
print(mensagem)  # Saída: Minha idade é: 25

# Atualizando o valor da variável idade
idade = 30
print(idade)  # Saída: 30

# Criando uma variável chamada 'msg'
msg = 'Olá, mundo!'
print(msg) # Saída: Olá, mundo!

## Tipos de dados

<a name="tipos-de-dados"></a>


esta seção, vamos praticar como criar variáveis em Python. As variáveis são usadas para armazenar e representar valores em nosso código.