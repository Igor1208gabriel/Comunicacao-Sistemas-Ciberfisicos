Repositório central para o projeto de pesquisa "Técnicas e ferramentas para modelagem e análise de comunicação em sistemas ciberfísicos" (7532/2024) IFRN/CNAT

# Comunicação em Sistemas Ciberfísicos

Este repositório está associado ao projeto de pesquisa **“Técnicas e ferramentas para modelagem e análise de comunicação em sistemas ciberfísicos”**, desenvolvido no IFRN/CNAT nos laboratórios LADES e LAICA.

O trabalho investiga a comunicação em Sistemas Ciberfísicos (SCFs), com foco em aplicações robóticas, explorando o uso da linguagem de modelagem **AADL (Architecture Analysis and Design Language)** e o framework **ROS2 (Robot Operating System)** para análise, modelagem e integração de microcontroladores e sistemas robóticos.

---

## 🚀 Objetivos

* **Geral:** Identificar e desenvolver técnicas e ferramentas para modelagem e análise de comunicação em SCFs.
* **Específicos:**

  1. Desenvolver ferramentas de modelagem e análise utilizando AADL em sistemas ROS2.
  2. Implementar e testar a comunicação direta entre microcontroladores e ROS2.
  3. Analisar a performance e a confiabilidade da comunicação em SCFs com técnicas de simulação.
  4. Explorar geração automática de código a partir de modelos AADL para facilitar a implementação.

---

## 📚 Fundamentação

* **SCFs:** Integração de processos físicos e computacionais.
* **ROS2:** Middleware para comunicação distribuída em sistemas robóticos. https://docs.ros.org/en/kilted/index.html
* **AADL:** Linguagem para modelagem arquitetural, análise de desempenho e confiabilidade. - https://www.sei.cmu.edu/projects/architecture-analysis-and-design-language-aadl/
* **OSATE2:** Ferramenta de apoio para análise e geração automática de código. - https://osate.org/

---

## 🛠️ Tecnologias

* **Linguagem:** Python, C++
* **Ferramentas:** ROS2, Arduino/ESP32, RAMSES2
* **Modelagem:** AADL, OSATE2
* **Plataformas:** Ubuntu 24, ROS2 Kilted Kaiju, simulações com Gazebo, visualização com RQT

---

## 📂 Estrutura do Repositório

```
/
├── aadl/workspace     # Workspace AADL
├── ros2/workspace     # Pacotes ROS2 e nós de teste
├── LICENSE            # Arquivo de Licensa de Software
└── README.md          # Este arquivo
```

---

## 🔬 Metodologia

1. Levantamento bibliográfico sobre SCFs, ROS2 e AADL.
2. Modelagem de sistemas ciberfísicos com AADL.
3. Implementação experimental com microcontroladores (Arduino/ESP32) e ROS2.
4. Simulações para avaliação de desempenho e confiabilidade.
5. Geração automática de código com OSATE2 e RAMSES2.
6. Testes experimentais e publicação dos resultados.

---

## ✅ Resultados Esperados

* **Metodológicos:** Modelos de referência em AADL, ferramentas de análise, processos de geração automática de código.
* **Técnicos:** Integração eficiente de microcontroladores com ROS2, desempenho otimizado, protótipos funcionais.
* **Acadêmicos:** Publicações científicas, relatório técnico, base para pesquisas futuras.

---

## 🌱 Contribuindo

1. Abra uma *issue* descrevendo a tarefa ou melhoria.
2. Crie uma *branch* a partir da `dev`.
3. Use **commits semânticos** (ex: `docs: atualizar README com objetivos do projeto`).
4. Faça um *pull request* para revisão.
5. Após aprovação, faça o *merge* na `dev`.

---

## 🔄 GitHub Flow no Projeto

* **Branch principal:** `main` sempre estável.
* **Fluxo:** `issue` → `branch` → `commits` → `pull request` → `merge`.
* **Commits semânticos:**

  * `feat:` nova funcionalidade
  * `fix:` correção de bug
  * `docs:` mudanças na documentação
  * `chore:` tarefas de manutenção

---

## 📜 Licença

Distribuído sob licensa personalizada. Consulte `LICENSE` para mais informações.
