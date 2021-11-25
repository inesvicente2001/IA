%privilegiar sempre o meio de entrega mais ecológico
%meios de transporte: bicicletas, motos e carros

estafeta([encomenda(Peso, Volume, transporte(Transporte), Prazo, rua(Rua,freguesia(Freguesia)), cliente(Cliente), Dia, Entregue, Classificacao)]).
%cliente([encomenda(estafeta(Estafeta),Peso, Volume, transporte(Transporte), Prazo, rua(Rua,freguesia(Freguesia)), cliente(Cliente), Dia, Entregue)]).
%preco(encomenda(estafeta(Estafeta),Peso, Volume, transporte(Transporte), Prazo, rua(Rua,freguesia(Freguesia)), cliente(Cliente), Dia, Entregue)).

%retirar_elementos([],[],[]).
%retirar_elementos(L2,[H|T],L1) :-
%    pertence(H,L1),
%    \+ (pertence(H,L2)),
%    retirar_elementos(L2,T,L1).
%retirar_elementos(L2,[H|T],L1) :-
%    pertence(H,L2),
%    \+ (pertence(H,L1)),
%    retirar_elementos(L2,T,L1).

%transporte(tipo, velocidade, capacidade, ecologicidade)
transporte( bicicleta, 10, 5, 2 ).
transporte( moto, 35, 20, 1 ).
transporte( carro, 25, 100, 0 ).

%encomenda_mais_ecologica(E1(_,_,),E2) :-



%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico;
%estafeta_mais_ecologico2(Hest[Enc1(_,_,T1,_,_,_,_,_)],Est[Enc2(_,_,T2,_,_,_,_,_)])
%
%estafeta_mais_ecologico(Est,[Est]).
%estafeta_mais_ecologico(Est,[Hest|Test]) :-
%    pertence(Est,[Hest|Test]),
%    estafeta_mais_ecologico2(Est,Hest),
%    estafeta_mais_ecologico(Est,[Test]).

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

uma_encomenda_por_estafeta(estafeta(LEncomenda),[],Cliente).
uma_encomenda_por_estafeta(estafeta(LEncomendaE),[HEncomenda|TEncomenda],Cliente) :-
    cliente(HEncomenda,Cliente),
    pertence(HEncomenda,LEncomendaE),
    uma_encomenda_por_estafeta(estafeta(LEncomendaE),TEncomenda,Cliente).

cliente(encomenda(_,_,_,_,_,Cliente,_,_,_),Cliente).

estafetas_entregaram3(LEstafeta,[]).
estafetas_entregaram3(LEstafeta,[HEncomenda|TEncomenda]) :-
    um_estafeta_por_encomenda(LEstafeta,HEncomenda),
    estafetas_entregaram3(LEstafeta,TEncomenda).

um_estafeta_por_encomenda([],Encomenda) :- false.
um_estafeta_por_encomenda([estafeta(LEncomendaE)|TEstafeta],Encomenda) :-
    pertence(Encomenda,LEncomendaE).
um_estafeta_por_encomenda([HEstafeta|TEstafeta],Encomenda) :-
    um_estafeta_por_encomenda(TEstafeta,Encomenda).

pertence( X,[X|L] ).
pertence( X,[Y|L] ) :-
    X \= Y,
    pertence( X,L ).

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar os clientes servidos por um determinado estafeta;

clientes_servidos([],estafeta([])).
clientes_servidos(LCliente,estafeta([encomenda(_,_,_,_,_,C,_,_,_)|Tencomenda])) :-
    pertence(C,LCliente),
    clientes_servidos(LCliente,estafeta(Tencomenda)).

%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o valor faturado pela Green Distribution num determinado dia;

faturado(0,Dia,[]).
faturado(Valor,Dia,[estafeta(LEncomenda)|TEstafeta]) :-
    faturado(Valor2,Dia,TEstafeta),
    faturado_estafeta(Valor1,Dia,LEncomenda),
    Valor is Valor1 + Valor2.

faturado_estafeta(0,Dia,[]).
faturado_estafeta(Valor,Dia,[encomenda(Peso, Volume, transporte(Transporte), Prazo,_,_,Dia,_,_)|TEncomenda]) :-
    faturado_estafeta()
%%%FALTA ACABAR

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar quais as zonas (e.g., rua ou freguesia) com maior volume de entregas por parte da Green Distribution;


%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular a classificação média de satisfação de cliente para um determinado estafeta;


%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo;


%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o número total de entregas pelos estafetas, num determinado intervalo de tempo;


%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o número de encomendas entregues e não entregues pela Green Distribution, num determinado período de tempo;


%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o peso total transportado por estafeta num determinado dia.

peso_total(0, []).
peso_total(Peso, Dia, estafeta([encomenda(P,_,_,_,_,_,Dia,_,_)|Tencomenda])) :-
    peso_total(Peso1, estafeta(Tencomenda)),
    Peso is Peso1 + P.
peso_total(Peso, Dia, estafeta([encomenda(P,_,_,_,_,_,D,_,_)|Tencomenda])) :-
    Dia \= D,
    peso_total(Peso, estafeta(Tencomenda)).
