"""
Tentauppgifter:

Uppgift 1:
Scheme:

a)
sum-list (summera alla tal i en lista)

ex-anrop:
(sum-list '(2 3 9 8))
> 22

(define (sum-list lst)
    (define (sum-helper lst ans)
        (if (null? sum-list)
            ans
            (sum-helper (cdr lst) (+ ans (car lst)))))
    (sum-helper lst 0))

b)
digit-list(skriv in ett tal och återsänder en lista med alla siffror talet består av)

(quotient 10 2) => 5
(qotient 13 2) => 6
(remainder 7 3) => 1

(define (digit-list num)
    (define (digit-helper num lst)
        (if (< num 10)
            (cons num lst)
            (digit-helper (quotient num 10) (cons (remainder num 10) lst))))
    (digit-helper num '()))

(digit-list 2398)
(helper 239 '(8))
(helper 23 '(9 8))
(helper 2 '(3 9 8))
'(2 3 9 8)

c)
(repeated-digitsum 2398) => (repeated-digitsum 22) => 4
görs mha a & b uppgiften.

(define (repeated-digitsum n)
    (if (< n 10)
        sum
        (repeated-digitsum (sum-list (digit-list n)))))

d)
Föreslå black-box tester för repeated-dititsum.
(r-d-s 0) => 0
(r-d-s 1) => 1
(r-d-s 2398) => 4
(r-d-s -21) => odefinierat

e)
Förklara hur man avgör om funktion är svansrekursiv eller ej.
I svansrekursiv uppdateras det som ska bli svaret inuti funktionen, i icke-svansrekursiva ligger beräkningar och väntar
utanför tills dess att den rekursiva funktionen uppnår ett basfall, och då sker alla beräkningar.

Uppgift 2)
Scheme

Teaterbiljetter.
((10 2 95) (10 3 60) (10 4 95) (5 2 70) (5 15 60) ...) där varje inre lista innehåller radnummer, stolsnummer och pris.

a) beskriv selektorer och selektorer för posten.

Konstruktor:
(define (make-post radnr, platsnr, pris)
    (list radnr platsnr pris))

(define(radnr post)
    (car post))

(define (stolsnr post)
    (cadr post))

(define (pris post)
    (caddr post))

b)

(define (totalbelopp register rad))
    (if (null? register)
        0
        (if (= (radnr (car register)) rad)
            (+ (pris (car register)) (totalbelopp (cdr register) rad))
            (totalbelopp (cdr register) rad))))

c)
Skriv en procedur som kollar så att det inte finns två poster med samma rad och stolsnr. Återsänder #t eller #f
beroende på om registret är korrekt eller ej.

(define (verify-register register)
    (define (inte-finns? rdnr pltsnr register)
        (cond ((null? register) #t)
              ((and (= pltsnr (platsnr (car register))) (= rdnr (radnr (car register)))) #f)
              (else (inte-finns? rdnr pltsnr (cdr register)))))
    (cond ((null? register) #t)
          ((intefinns? (radnr (car register)) (platsnr(car register))(cdr register))
              (verify-register (cdr register)))
          (else #f)))

d) Det blir tydligare av namnen, exakt vad man gör.

Uppgift 3)
Python, transponera matriser:
[[1, 2, 3], [4, 5, 6]] => [[1, 4], [2, 5], [3, 6]]

def transponera(lst):
    utlista = []
    kolumn = len(lst[0])
    i = 0
    while i < kolumn:
        tmp = []
        for rad in lst:
            tmp.append([rad[i]])
        utlista.append(tmp)
        1 += 1
    return utmatris

Uppgift 4)
Python
korsordhanterare:

a n t i k
v i _ s _
s o t _ t
t _ å k a
å _ g o l

facit = {(1,1,’h’):’antik’, (2,1,’h’):’vi’,
        (3,1,’h’):’sot’, (4,3,’h’):’åka’,
        (5,1,’h’):’å’, (5,3,’h’):’gol’,
        (1,1,’v’):’avstå’, (1,2,’v’):’nio’,
        (3,3,’v’):’tåg’, (1,4,’v’):’is’,
        (4,4,’v’):’ko’, (3,5,’v’):’tal’}


from facitfil import facit
fil = open("korsord.txt")
allarader = fil.readlines()
allakolumner = transponera(allarader)
allarader = map(list, allarader)
"""