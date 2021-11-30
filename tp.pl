%classificação (-1) significa que não foi entregue
%o prazo de entrega é em horas
estafeta(Nome,[encomenda(Peso, Volume, Transporte, Prazo, rua(Rua,Freguesia), cliente(Cliente), tempo(Dia,Hora), Classificacao)]).

velocidade(bicicleta, 10).
velocidade(mota, 35).
velocidade(carro, 25).

capacidade(bicicleta, 5).
capacidade(mota, 20).
capacidade(carro, 100).

ecologicidade(bicicleta, 2).
ecologicidade(mota, 1).
ecologicidade(carro, 0).

%aqui vai estar o conjunto de freguesias e, dentro de cada freguesia, as suas ruas


%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;

% estafeta tem de pertencer à lista
% estafeta tem de ser mais (ou igualmente) ecológico que todos os da lista

estafeta_mais_ecologico(Estafeta,LEstafeta) :-
    pertence(Estafeta,LEstafeta),
    estafeta_mais_ecologico2(Estafeta,LEstafeta).

estafeta_mais_ecologico2(estafeta(_,LEncomenda1),[estafeta(_,LEncomenda2)]) :-
    mais_ecologico(N,LEncomenda1,LEncomenda2),
    N >= 0.
estafeta_mais_ecologico2(estafeta(_,LEncomenda1),[estafeta(_,LEncomenda2)|TEstafeta]) :-
    mais_ecologico(N,LEncomenda1,LEncomenda2),
    N >= 0,
    estafeta_mais_ecologico2(estafeta(_,LEncomenda1),TEstafeta).

mais_ecologico(0,[],[]).
mais_ecologico(N,[encomenda(_,_,tr1,_,_,_,_,_)|TEncomenda],[]) :-
    ecologicidade(tr1,N1),
    mais_ecologico(N2,TEncomenda,[]),
    N is N2 + N1.
mais_ecologico(N,[],[encomenda(_,_,tr2,_,_,_,_,_)|TEncomenda]) :-
    ecologicidade(tr1,N1),
    mais_ecologico(N2,[],TEncomenda),
    N is N2 - N1.
mais_ecologico(N,[encomenda(_,_,tr1,_,_,_,_,_)|TEncomenda1],[encomenda(_,_,tr2,_,_,_,_,_)|TEncomenda2]) :-
    ecologicidade(tr1,N1),
    ecologicidade(tr2,N2),
    mais_ecologico(N3,TEncomenda1,TEncomenda2),
    N is (N3 + N1 - N2).

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar que estafetas entregaram determinada(s) encomenda(s) a um determinado cliente;

% a lista de encomendas é para o Cliente
% toda a lista de estafetas tem pelo menos uma encomenda cada um
% não há encomendas sem estafeta

estafetas_entregaram(LEstafeta,LEncomenda,Cliente) :-
    estafetas_entregaram2(LEstafeta,LEncomenda,Cliente),
    estafetas_entregaram3(LEstafeta,LEncomenda).

estafetas_entregaram2([],[],Cliente).
estafetas_entregaram2([HEstafeta|TEstafeta],LEncomenda,Cliente) :-
    uma_encomenda_por_estafeta(LEncomenda,HEstafeta,Cliente),
    estafetas_entregaram2(TEstafeta,LEncomenda,Cliente).

uma_encomenda_por_estafeta(LEncomenda,[],Cliente).
uma_encomenda_por_estafeta(LEncomendaE,[HEncomenda|TEncomenda],Cliente) :-
    cliente(HEncomenda,Cliente),
    pertence(HEncomenda,LEncomendaE),
    uma_encomenda_por_estafeta(LEncomendaE,TEncomenda,Cliente).

cliente(encomenda(_,_,_,_,_,Cliente,_,Class),Cliente) :-
    Class \= (-1).

estafetas_entregaram3(LEstafeta,[]).
estafetas_entregaram3(LEstafeta,[HEncomenda|TEncomenda]) :-
    um_estafeta_por_encomenda(LEstafeta,HEncomenda),
    estafetas_entregaram3(LEstafeta,TEncomenda).
    
um_estafeta_por_encomenda([estafeta(_,LEncomendaE)|TEstafeta],Encomenda) :-
    pertence(Encomenda,LEncomendaE).
um_estafeta_por_encomenda([HEstafeta|TEstafeta],Encomenda) :-
    um_estafeta_por_encomenda(TEstafeta,Encomenda).

pertence( X,[X|L] ).
pertence( X,[Y|L] ) :-
    X \= Y,
    pertence( X,L ).

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar os clientes servidos por um determinado estafeta;

% todos os clientes da lista de encomendas têm de estar na lista de clientes
% todos os clientes da lista de clientes têm de estar na lista de encomendas

clientes_servidos(LCliente,estafeta(_,LEncomenda)) :-
    clientes_servidos1(LCliente,LEncomenda),
    clientes_servidos2(LCliente,LEncomenda).

clientes_servidos1([],[]).
clientes_servidos1(LCliente,[encomenda(_,_,_,_,_,C,_,_)|Tencomenda]) :-
    pertence(C,LCliente),
    clientes_servidos1(LCliente1,Tencomenda).

clientes_servidos2([],[]).
clientes_servidos2([HCliente|TCliente],LEncomenda) :-
    pertence_lista_encomendas(HCliente,LEncomenda),
    clientes_servidos2(TCliente,LEncomenda).

pertence_lista_encomendas(Cliente,[encomenda(_,_,_,_,_,Cliente,_,_)|Tencomenda]).
pertence_lista_encomendas(Cliente,[encomenda(_,_,_,_,_,C,_,_)|Tencomenda]) :-
    Cliente \= C,
    pertence_lista_encomendas(Cliente,TEncomenda).

%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o valor faturado pela Green Distribution num determinado dia;

faturado(0,Dia,[]).
faturado(Valor,Dia,[estafeta(LEncomenda)|TEstafeta]) :-
    faturado(Valor1,Dia,TEstafeta),
    faturado_estafeta(Valor2,Dia,LEncomenda),
    Valor is Valor1 + Valor2.

%O preço do serviço de entrega deverá ter em conta para além da encomenda, pelo menos, o prazo de entrega e meio de transporte utlizado.

faturado_estafeta(0,Dia,[]).
faturado_estafeta(Valor,Dia,[encomenda(_,_,_,_,_,_,tempo(Dia,_),_)|TEncomenda]) :-
    faturado_estafeta(Valor1,Dia,TEncomenda),
    preco_encomenda(Valor2,encomenda(_,_,_,_,_,_,tempo(Dia,_),_)),
    Valor is Valor1 + Valor2.
faturado_estafeta(Valor,Dia,[encomenda(_,_,_,_,_,_,tempo(D,_),_)|TEncomenda]) :-
    Dia \= D,
    faturado_estafeta(Valor,Dia,TEncomenda).

% o preço aumenta quanto:
    % maior for o peso
    % maior for o volume
    % menos ecológico for o veículo: carro > mota > bicicleta
    % menor for o prazo
preco_encomenda(Valor,encomenda(Peso, Volume, carro, Prazo,_,_,_,_)) :-
    Valor = (20 * Peso * Volume) / Prazo.
preco_encomenda(Valor,encomenda(Peso, Volume, mota, Prazo,_,_,_,_)) :-
    Valor = (15 * Peso * Volume) / Prazo.
preco_encomenda(Valor,encomenda(Peso, Volume, bicicleta, Prazo,_,_,_,_)) :-
    Valor = (10 * Peso * Volume) / Prazo.
preco_encomenda(0,encomenda(Peso, Volume, carro, Prazo,_,_,_,(-1))).
%%%REVER VALORES PARA VER SE FAZEM SENTIDO

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar quais as zonas (e.g., rua ou freguesia) com maior volume de entregas por parte da Green Distribution;

%vamos ter de percorrer toda a lista de freguesias/ruas, e verificar que a selecionada é a que tem mais entregas

zona_maior_entrega(rua,rua(_,N),[freguesia(LRua,_)]) :-
    zona_maior_entrega_freguesia(rua(_,N),LRua).
zona_maior_entrega(freguesia,freguesia(_,N1),[freguesia(_,N2)]) :-
    N1 >= N2.
zona_maior_entrega(rua,rua(_,N),[freguesia(LRua,_)|TFreguesia]) :-
    zona_maior_entrega_freguesia(rua(_,N),LRua),
    zona_maior_entrega(rua,rua(_,N),TFreguesia).
zona_maior_entrega(freguesia,freguesia(_,N1),[freguesia(_,N2)|TFreguesia]) :-
    N1 >= N2,
    zona_maior_entrega(freguesia,freguesia(_,N1),TFreguesia).

zona_maior_entrega_freguesia(rua(_,N),[rua(_,N2)|TRua]) :-
    N1 >= N2,
    zona_maior_entrega_freguesia(rua(_,N),TRua).

%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular a classificação média de satisfação de cliente para um determinado estafeta;

satisfação(Media,Cliente,estafeta(_,LEncomenda)) :-
    satisfacao_aux(Media,N,Cliente,LEncomenda),
    numero_encomendas(N,Cliente,LEncomenda).

satisfacao_aux(0,0,Cliente,[]).
satisfacao_aux(Media,N,Cliente,[encomenda(_,_,_,_,_,Cliente,_,Classificacao)|TEncomenda]) :-
    satisfacao_aux(Media1,N1,Cliente,TEncomenda),
    N is N1 + 1,
    Media is ((Media1 * N1 + Classificacao)/N).
satisfacao_aux(Media,N,Cliente,[encomenda(_,_,_,_,_,C,_,Classificacao)|TEncomenda]) :-
    Cliente \= C,
    satisfacao_aux(Media,N,Cliente,TEncomenda).

numero_encomendas(0,_,[]).
numero_encomendas(N,Cliente,[encomenda(_,_,_,_,_,C,_,_)|TEncomenda]) :-
    Cliente \= C,
    numero_encomendas(N,Cliente,TEncomenda).
numero_encomendas(N,Cliente,[encomenda(_,_,_,_,_,Cliente,_,_)|TEncomenda]) :-
    numero_encomendas(N1,Cliente,TEncomenda),
    N is N1 + 1.

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo;

entregas_por_transporte(0,0,0,_,_,[]).
entregas_por_transporte(Carro,Mota,Bicicleta,Inicio,Fim,[estafeta(LEncomenda)|TEstafeta]) :-
    entregas_por_transporte_estafeta(Carro1,Mota1,Bicicleta1,Inicio,Fim,LEncomenda),
    entregas_por_transporte(Carro2,Mota2,Bicicleta2,Inicio,Fim,[HEstafeta|TEstafeta]),
    Carro is Carro1 + Carro2,
    Mota is Mota1 + Mota2,
    Bicicleta is Bicicleta1 + Bicicleta2.

entregas_por_transporte_estafeta(0,0,0,_,_,[]).
entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,[encomenda(_,_,carro,_,_,_,Tempo,Class)|TEncomenda]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    Class \= (-1),
    entregas_por_transporte_estafeta(Carro1,Mota,Bicicleta,Inicio,Fim,TEncomenda),
    Carro is Carro1 + 1.
entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,[encomenda(_,_,mota,_,_,_,Tempo,Class)|TEncomenda]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    Class \= (-1),
    entregas_por_transporte_estafeta(Carro,Mota1,Bicicleta,Inicio,Fim,TEncomenda),
    Mota is Mota1 + 1.
entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,[encomenda(_,_,bicicleta,_,_,_,Tempo,Class)|TEncomenda]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    Class \= (-1),
    entregas_por_transporte_estafeta(Carro,Mota,Bicicleta1,Inicio,Fim,TEncomenda),
    Bicicleta is Bicicleta1 + 1.
entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,Class)|TEncomenda]) :-
    \+ (pertence_tempo(Inicio,Fim,Tempo)),
    entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,TEncomenda).
entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,Class)|TEncomenda]) :-
    Class = (-1),
    entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,TEncomenda).

pertence_tempo(tempo(DiaI,HoraI),tempo(DiaF,HoraF),tempo(Dia,Hora)) :-
    Dia > DiaI,
    Dia < DiaF.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaI,HoraF),tempo(DiaI,Hora)) :-
    Hora >= HoraI,
    Hora =< HoraF.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaF,HoraF),tempo(DiaI,Hora)) :-
    DiaI > DiaF,
    Hora >= HoraI.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaF,HoraF),tempo(DiaF,Hora)) :-
    DiaI > DiaF,
    Hora =< HoraF.

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o número total de entregas pelos estafetas, num determinado intervalo de tempo;

entregas_totais(0,_,_,[]).
entregas_totais(Valor,Inicio,Fim,[estafeta(_,LEncomenda)|TEstafeta]) :-
    entregas_totais_estafeta(Valor1,Inicio,Fim,LEncomenda),
    entregas_totais(Valor2,Inicio,Fim,TEstafeta),
    Valor is Valor1 + Valor2.

entregas_totais_estafeta(0,_,_,[]).
entregas_totais_estafeta(Valor,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,Class)|TEncomenda]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    Class \= (-1),
    entregas_totais_estafeta(Valor1,Inicio,Fim,TEncomenda),
    Valor is Valor1 + 1.
entregas_totais_estafeta(Valor,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,Class)|TEncomenda]) :-
    \+ (pertence_tempo(Inicio,Fim,Tempo)),
    entregas_totais_estafeta(Valor,Inicio,Fim,TEncomenda).
entregas_totais_estafeta(Valor,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,Class)|TEncomenda]) :-
    Class = (-1),
    entregas_totais_estafeta(Valor,Inicio,Fim,TEncomenda).


%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o número de encomendas entregues e não entregues pela Green Distribution, num determinado período de tempo;

entregues_ou_nao(0,0,_,_,[]).
entregues_ou_nao(Entregues,NaoEntregues,Inicio,Fim,[estafeta([LEncomenda])|TEstafeta]) :-
    entregues_ou_nao_estafeta(Entregues1,NaoEntregues1,Inicio,Fim,LEncomenda),
    entregues_ou_nao(Entregues2,NaoEntregues2,Inicio,Fim,LEncomenda),
    Entregues is Entregues1 + Entregues2,
    NaoEntregues is NaoEntregues1 + NaoEntregues2.

entregues_ou_nao_estafeta(0,0,_,_,[]).
entregues_ou_nao_estafeta(Entregues,NaoEntregues,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,Class)|TEncomenda]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    Class = (-1),
    entregues_ou_nao_estafeta(Entregues,NaoEntregues1,Inicio,Fim,TEncomenda),
    NaoEntregues is NaoEntregues1 + 1.
entregues_ou_nao_estafeta(Entregues,NaoEntregues,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,Class)|TEncomenda]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    Class \= (-1),
    entregues_ou_nao_estafeta(Entregues1,NaoEntregues,Inicio,Fim,TEncomenda),
    Entregues is Entregues1 + 1.
entregues_ou_nao_estafeta(Entregues,NaoEntregues,Inicio,Fim,[encomenda(_,_,_,_,_,_,Tempo,_)|TEncomenda]) :-
    \+ (pertence_tempo(Inicio,Fim,Tempo)),
    entregues_ou_nao_estafeta(Entregues,NaoEntregues,Inicio,Fim,TEncomenda).


%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o peso total transportado por estafeta num determinado dia.

peso_total(0, []).
peso_total(Peso, Dia, estafeta(_,[encomenda(P,_,_,_,_,_,tempo(Dia,_),_)|Tencomenda])) :-
    peso_total(Peso1, estafeta(_,Tencomenda)),
    Peso is Peso1 + P.
peso_total(Peso, Dia, estafeta(_,[encomenda(P,_,_,_,_,_,tempo(D,_),_)|Tencomenda])) :-
    Dia \= D,
    peso_total(Peso, estafeta(_,Tencomenda)).
