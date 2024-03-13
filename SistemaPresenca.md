## 2 Diagrama de caso de uso
```plantuml
@startuml
left to right direction

actor Diretoria as diretoria
actor Professores as professores
actor Coordenadoria as coordenadoria
actor Estudantes as estudantes
actor Pais_de_Alunos as pais

rectangle Sistema_de_Presenças {
    diretoria -- (Visualizar_total)
    diretoria -- (Controle_total)
    professores -- (Enviar_mensagem_para_aluno)
    professores -- (Enviar_mensagem_para_pais)
    professores -- (Marcar_presenças)
    coordenadoria -- (Contato_com_professores)
    coordenadoria -- (Contato_com_pais)
    estudantes -- (Visualizar_notificações)
    estudantes -- (Visualizar_datas_de_provas)
    estudantes -- (Visualizar_materiais_solicitados)
    pais -- (Acompanhar_presença_estudante)
    pais -- (Visualizar_avaliações)
    pais -- (Visualizar_notificações)
}

@enduml
```

## 3 Modelo de dominio
```plantuml
@startuml
package "Escola" {
    class Aluno {
        - id: int
        - nome: String
        - dataNascimento: Date
        - genero: String
        - turma: Turma
        - presencas: List<Presenca>
    }

    class Professor {
        - id: int
        - nome: String
        - disciplina: String
        - turmas: List<Turma>
    }

    class Turma {
        - id: int
        - nome: String
        - alunos: List<Aluno>
        - professor: Professor
    }

    class Presenca {
        - id: int
        - data: Date
        - presente: boolean
        - aluno: Aluno
    }
}

Aluno --|> Presenca
Turma "1" --* "0..*" Aluno
Turma "1" -- "1" Professor
@enduml
```

## 4 Diagrama de sequencias

## 4.1 Diretoria
```plantuml
@startuml
hide footbox

actor "Dispositivo do Diretoria" as dir
participant "Sistema de\nGerenciamento de\nPresenças" as sistema
database "Servidor de\nBanco de Dados" as servidor

dir -> sistema: Iniciar sessão
activate sistema
sistema -> servidor: Verificar credenciais
activate servidor
sistema <-- servidor: Responder com status da autenticação
deactivate servidor
sistema -> servidor: Solicitar lista de aulas
activate servidor
sistema <-- servidor: Recuperar lista de aulas
deactivate servidor
sistema --> dir: Enviar lista de aulas
dir -> sistema: Marcar presença em uma aula
activate sistema
sistema -> servidor: Atualizar presença
activate servidor
sistema <-- servidor: Confirmar atualização
deactivate servidor
sistema --> dir: Confirmar atualização
deactivate sistema
dir -> sistema: Envia mensagens para Alunos/Pais/Prof
activate sistema
sistema --> dir: Confirmação de envio
deactivate sistema
dir -> sistema: Visualizar notificações
activate sistema
sistema --> dir: Lista de notificações
deactivate sistema
dir -> sistema: Visualizar datas das provas
activate sistema
sistema --> dir: Calendário de provas
deactivate sistema
dir -> sistema: Visualizar materiais solicitados pelos professores
activate sistema
sistema --> dir: Lista de materiais solicitados
deactivate sistema
deactivate dir

@enduml
```

## 4.2 Professor
```plantuml
@startuml
hide footbox

actor "Dispositivo do Professor" as prof
participant "Sistema de\nGerenciamento de\nPresenças" as sistema
database "Servidor de\nBanco de Dados" as servidor

prof -> sistema: Iniciar sessão
activate sistema
sistema -> servidor: Verificar credenciais
activate servidor
sistema <-- servidor: Responder com status da autenticação
deactivate servidor
sistema -> servidor: Solicitar lista de aulas
activate servidor
sistema <-- servidor: Recuperar lista de aulas
deactivate servidor
sistema --> prof: Enviar lista de aulas
prof -> sistema: Marcar presença em uma aula
activate sistema
sistema -> servidor: Atualizar presença
activate servidor
sistema <-- servidor: Confirmar atualização
deactivate servidor
sistema --> prof: Confirmar atualização
deactivate sistema
prof -> sistema: Envia mensagens para Alunos/Pais
activate sistema
sistema --> prof: Confirmação de envio
deactivate sistema

@enduml
```

## 4.3 Coordenadoria
```plantuml
@startuml
hide footbox

actor "Dispositivo do Coordenadoria" as coor
participant "Sistema de\nGerenciamento de\nPresenças" as sistema
database "Servidor de\nBanco de Dados" as servidor

coor -> sistema: Iniciar sessão
activate sistema
sistema -> servidor: Verificar credenciais
activate servidor
sistema <-- servidor: Responder com status da autenticação
deactivate servidor
coor -> sistema: Envia mensagens para Prof/Pais
activate sistema
sistema --> coor: Confirmação de envio
deactivate sistema

@enduml
```

## 4.4 Aluno
```plantuml
@startuml
hide footbox

actor "Dispositivo do Aluno" as aluno
participant "Sistema de\nGerenciamento de\nPresenças" as sistema
database "Servidor de\nBanco de Dados" as servidor

activate aluno
aluno -> sistema: Iniciar sessão
activate sistema
sistema -> servidor: Verificar credenciais
activate servidor
sistema <-- servidor: Responder com status da autenticação
deactivate servidor
sistema -> servidor: Solicitar lista de aulas
activate servidor
sistema <-- servidor: Recuperar lista de aulas
deactivate servidor
sistema --> aluno: Enviar lista de aulas
aluno -> sistema: Visualizar notificações
activate sistema
sistema --> aluno: Lista de notificações
deactivate sistema
aluno -> sistema: Visualizar datas das provas
activate sistema
sistema --> aluno: Calendário de provas
deactivate sistema
aluno -> sistema: Visualizar materiais solicitados pelos professores
activate sistema
sistema --> aluno: Lista de materiais solicitados
deactivate sistema
deactivate aluno

@enduml
```

## 4.5 Pais de Alunos
```plantuml
@startuml
hide footbox

actor "Dispositivo do Pais" as pais
participant "Sistema de\nGerenciamento de\nPresenças" as sistema
database "Servidor de\nBanco de Dados" as servidor

activate pais
pais -> sistema: Iniciar sessão
activate sistema
sistema -> servidor: Verificar credenciais
activate servidor
sistema <-- servidor: Responder com status da autenticação
deactivate servidor
pais -> sistema: Visualizar notificações
activate sistema
sistema --> pais: Lista de notificações
deactivate sistema
pais -> sistema: Visualizar datas das provas
activate sistema
sistema --> pais: Calendário de provas
deactivate sistema
pais -> sistema: Acompanhar a presença dos alunos
activate sistema
sistema --> pais: Lista de presença dos alunos
deactivate sistema
deactivate pais

@enduml
```

## 5 Diagrama de sequencia do sistema
```plantuml
@startuml
hide footbox

actor "Dispositivo do Aluno" as aluno
actor "Dispositivo do Professor" as prof
actor "Dispositivo da Coordenadoria" as coor
actor "Dispositivo dos Pais de Alunos" as pais

participant "Sistema de\nGerenciamento de\nPresenças" as sistema
database "Servidor de\nBanco de Dados" as servidor

== Autenticação ==
aluno -> sistema: Iniciar sessão
prof -> sistema: Iniciar sessão
coor -> sistema: Iniciar sessão
pais -> sistema: Iniciar sessão

== Outras interações ==
aluno -> sistema: Visualizar notificações
prof -> sistema: Marcar presença em aula
coor -> sistema: Entrar em contato com Professor
pais -> sistema: Visualizar presença do Aluno

== Registro de presença ==
prof -> sistema: Registrar presença

@enduml
```

## 6 Diagrama de classes de projeto
```plantuml
@startuml

class Aluno {
    - nome: String
    - matricula: String
    - presenca: boolean
    + marcarPresenca(): void
}

class Professor {
    - nome: String
    - disciplina: String
    + enviarMensagem(aluno: Aluno, mensagem: String): void
    + enviarMensagem(pais: PaisDeAluno, mensagem: String): void
}

class Coordenadoria {
    - nome: String
    + entrarEmContato(professor: Professor, mensagem: String): void
    + enviarMensagem(pais: PaisDeAluno, mensagem: String): void
}


class PaisDeAlunos {
    - nome: String
    - aluno: Aluno
    + visualizarPresenca(): void
}

class SistemaDePresencas {
    - alunos: List<Aluno>
    - professores: List<Professor>
    - coordenadores: List<Coordenadoria>
    + adicionarAluno(aluno: Aluno): void
    + adicionarProfessor(professor: Professor): void
    + adicionarCoordenador(coordenador: Coordenadoria): void
}


Aluno "*" *-- "1" PaisDeAlunos
Professor "1" *-- "*" Aluno
Coordenadoria "1" *-- "*" Professor
SistemaDePresencas "1" *-- "0..*" Aluno
SistemaDePresencas "1" *-- "0..*" Professor
SistemaDePresencas "1" *-- "0..*" Coordenadoria

@enduml
```