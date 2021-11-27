%classificação 0 significa que não foi entregue
%o prazo de entrega é em horas
estafeta([encomenda_entregue(Peso, Volume, transporte(Transporte), Prazo, rua(Rua,Freguesia), cliente(Cliente), tempo(Dia,Hora), Classificacao)]).

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

%aqui vai estar o conjunto de freguesias e, dentro de cada freguesia, as suas ruas

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

cliente(encomenda(_,_,_,_,_,Cliente,_,Class),Cliente) :-
    \+ (Class = 0).

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
clientes_servidos(LCliente,estafeta([encomenda(_,_,_,_,_,C,_,_)|Tencomenda])) :-
    pertence(C,LCliente),
    clientes_servidos(LCliente,estafeta(Tencomenda)).

%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o valor faturado pela Green Distribution num determinado dia;

faturado(0,Dia,[]).
faturado(Valor,Dia,[estafeta(LEncomenda|TEstafeta)]) :-
    faturado(Valor1,Dia,TEstafeta),
    faturado_estafeta(Valor2,Dia,LEncomenda),
    Valor is Valor1 + Valor2.

%O preço do serviço de entrega deverá ter em conta para além da encomenda, pelo menos, o prazo de entrega e meio de transporte utlizado.

faturado_estafeta(0,Dia,[]).
faturado_estafeta(Valor,Dia,[HEncomenda|TEncomenda]) :-
    faturado_estafeta(Valor1,Dia,TEncomenda),
    faturado_encomenda(Valor2,Dia,HEncomenda),
    Valor is Valor1 + Valor2.

% o preço aumenta quanto:
    % maior for o peso
    % maior for o volume
    % menos ecológico for o veículo: carro > mota > bicicleta
    % menor for o prazo
faturado_encomenda(Valor,Dia,encomenda(Peso, Volume, carro, Prazo,_,_,tempo(Dia,_),_)) :-
    Valor = (20 * Peso * Volume) / Prazo.
faturado_encomenda(Valor,Dia,encomenda(Peso, Volume, mota, Prazo,_,_,tempo(Dia,_),_)) :-
    Valor = (15 * Peso * Volume) / Prazo.
faturado_encomenda(Valor,Dia,encomenda(Peso, Volume, bicicleta, Prazo,_,_,tempo(Dia,_),_)) :-
    Valor = (10 * Peso * Volume) / Prazo.
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

satisfação(Media,Cliente,Estafeta) :-
    satisfacao_aux(Media,N,Cliente,Estafeta),
    numero_encomendas(N,Cliente,Estafeta).

satisfacao_aux(0,0,Cliente,estafeta([])).
satisfacao_aux(Media,N,Cliente,estafeta([encomenda(_,_,_,_,_,Cliente,_,Classificacao)|TEncomenda])) :-
    satisfacao_aux(Media1,N1,Cliente,estafeta(TEncomenda)),
    N is N1 + 1,
    Media is ((Media1 * N1 + Classificacao)/N).
satisfacao_aux(Media,N,Cliente,estafeta([encomenda(_,_,_,_,_,C,_,Classificacao)|TEncomenda])) :-
    Cliente \= C,
    satisfacao_aux(Media,N,Cliente,estafeta(TEncomenda)).

numero_encomendas(0,_,[]).
numero_encomendas(N,Cliente,estafeta([encomenda(_,_,_,_,_,C,_,_)|TEncomenda])) :-
    Cliente \= C,
    numero_encomendas(N,Cliente,TEncomenda).
numero_encomendas(N,Cliente,estafeta([encomenda(_,_,_,_,_,Cliente,_,_)|TEncomenda])) :-
    numero_encomendas(N1,Cliente,TEncomenda),
    N is N1 + 1.

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo;

entregas_por_transporte(0,0,0,_,_,[]).
entregas_por_transporte(Carro,Mota,Bicicleta,Inicio,Fim,[HEstafeta|TEstafeta]) :-
    entregas_por_transporte_estafeta(Carro1,Mota1,Bicicleta1,Inicio,Fim,HEstafeta),
    entregas_por_transporte(Carro2,Mota2,Bicicleta2,Inicio,Fim,[HEstafeta|TEstafeta]),
    Carro is Carro1 + Carro2,
    Mota is Mota1 + Mota2,
    Bicicleta is Bicicleta1 + Bicicleta2.

entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,estafeta([encomenda(_,_,carro,_,_,_,Tempo,Class)|TEncomenda)]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    entregas_por_transporte_estafeta(Carro1,Mota,Bicicleta,Inicio,Fim,estafeta([encomenda(TEncomenda)),
    Carro is Carro1 + 1.
entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,estafeta([encomenda(_,_,mota,_,_,_,Tempo,Class)|TEncomenda)]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    entregas_por_transporte_estafeta(Carro,Mota1,Bicicleta,Inicio,Fim,estafeta([encomenda(TEncomenda)),
    Mota is Mota1 + 1.
entregas_por_transporte_estafeta(Carro,Mota,Bicicleta,Inicio,Fim,estafeta([encomenda(_,_,bicicleta,_,_,_,Tempo,Class)|TEncomenda)]) :-
    pertence_tempo(Inicio,Fim,Tempo),
    entregas_por_transporte_estafeta(Carro,Mota,Bicicleta1,Inicio,Fim,estafeta([encomenda(TEncomenda)),
    Bicicleta is Bicicleta1 + 1.

pertence_tempo(tempo(DiaI,HoraI),tempo(DiaF,HoraF),tempo(Dia,Hora)) :-
    Dia > DiaI,
    Dia < DiaF.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaI,HoraF),tempo(DiaI,Hora)) :-
    Hora > HoraI,
    Hora < HoraF.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaF,HoraF),tempo(DiaI,Hora)) :-
    DiaI > DiaF,
    Hora > HoraI.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaF,HoraF),tempo(DiaF,Hora)) :-
    DiaI > DiaF,
    Hora < HoraF.

%------------------------------------------------------------------------------------------------------------------------------------------------
%identificar o número total de entregas pelos estafetas, num determinado intervalo de tempo;



%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o número de encomendas entregues e não entregues pela Green Distribution, num determinado período de tempo;


%------------------------------------------------------------------------------------------------------------------------------------------------
%calcular o peso total transportado por estafeta num determinado dia.

peso_total(0, []).
peso_total(Peso, Dia, estafeta([encomenda(P,_,_,_,_,_,tempo(Dia,_),_)|Tencomenda])) :-
    peso_total(Peso1, estafeta(Tencomenda)),
    Peso is Peso1 + P.
peso_total(Peso, Dia, estafeta([encomenda(P,_,_,_,_,_,tempo(D,_),_)|Tencomenda])) :-
    Dia \= D,
    peso_total(Peso, estafeta(Tencomenda)).
