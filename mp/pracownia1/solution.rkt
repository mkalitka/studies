#lang racket

(provide (struct-out column-info)
         (struct-out table)
         (struct-out and-f)
         (struct-out or-f)
         (struct-out not-f)
         (struct-out eq-f)
         (struct-out eq2-f)
         (struct-out lt-f)
         table-insert
         table-project
         table-sort
         table-select
         table-rename
         table-cross-join
         table-natural-join)

(define-struct column-info (name type) #:transparent)

(define-struct table (schema rows) #:transparent)


(define cities
  (table
   (list (column-info 'city 'string)
         (column-info 'country 'string)
         (column-info 'area 'number)
         (column-info 'capital 'boolean))
   (list (list "Wroclaw" "Poland" 293 #f)
         (list "Warsaw" "Poland" 517 #t)
         (list "Poznan" "Poland" 262 #f)
         (list "Berlin" "Germany" 892 #t)
         (list "Munich" "Germany" 310 #f)
         (list "Paris" "France" 105 #t)
         (list "Rennes" "France" 50 #f))))

(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define (empty-table columns) (table columns '()))



; Wstawianie

(define (get-type v)
  (cond
    [(number? v) 'number]
    [(string? v) 'string]
    [(symbol? v) 'symbol]
    [(boolean? v) 'boolean]
    [else 'unknown]))

(define (convert-table-to-types tab)
  (map (lambda (r) (column-info-type r)) (table-schema tab)))

(define (convert-row-to-types row)
  (map get-type row))

(define (table-insert row tab)
  (if (equal? (convert-row-to-types row) (convert-table-to-types tab))
      (table (table-schema tab) (append (table-rows tab) (list row)))
      (error "error: types not equal")))

;(table-insert (list "Amsterdam" "Netherlands" 18 #t) cities)



; Projekcja

(define (get-column-value sch name row)
  (if (empty? sch)
      '()
      (if (equal? (column-info-name (first sch)) name)
          (first row)
          (get-column-value (rest sch) name (rest row)))))

(define (table-project cols tab)
  (define (project-rows cols sch row)
    (if (or (empty? row) (empty? sch) (empty? cols))
        '()
        (if (equal? (first cols) (column-info-name (first sch)))
            (cons (first row) (project-rows (rest cols) (rest sch) (rest row)))
            (project-rows cols (rest sch) (rest row)))))
  (table (filter (lambda (c) (member (column-info-name c) cols)) (table-schema tab))
         (map (lambda (r) (project-rows cols (table-schema tab) r)) (table-rows tab))))

;(table-project '(city country) cities)


; Zmiana nazwy

(define (table-rename col ncol tab)
  (define (rename-col col ncol schema)
    (if (empty? schema)
        '()
        (if (equal? col (column-info-name (first schema)))
            (append (list (column-info ncol (column-info-type (first schema))))
                    (rest schema))
            (append (list (first schema)) (rename-col col ncol (rest schema))))))
  (table (rename-col col ncol (table-schema tab)) (table-rows tab)))

;(table-rename 'city 'name (table-insert (list "Amsterdam" "Netherlands" 18 #t) cities))


; Sortowanie

(define (types-compare< x y)
  (cond
    [(string? x) (string<? x y)]
    [(number? x) (< x y)]
    [(symbol? x) (symbol<? x y)]
    [(boolean? x) (and (equal? x #f) (equal? y #t))]))

(define (sort-helper row1 row2 cols sch)
  (cond
    [(empty? cols) #f]
    [(types-compare< (get-column-value sch (first cols) row1) (get-column-value sch (first cols) row2)) #t]
    [(equal? (get-column-value sch (first cols) row1) (get-column-value sch (first cols) row2)) (sort-helper row1 row2 (rest cols) sch)]
    [else #f]))

(define (table-sort cols tab)
  (table (table-schema tab) (sort (table-rows tab) (lambda (x y) (sort-helper x y cols (table-schema tab))))))

;(table-rows (table-sort '(country city) cities))
;(table-rows (table-sort '(country capital) cities))

; Selekcja

(define-struct and-f (l r))
(define-struct or-f (l r))
(define-struct not-f (e))
(define-struct eq-f (name val))
(define-struct eq2-f (name name2))
(define-struct lt-f (name val))

(define (table-select form tab)
  (define (get-val form row sch)
    (cond
      [(and-f? form) (and (get-val (and-f-l form) row sch) (get-val (and-f-r form) row sch))]
      [(or-f? form) (or (get-val (or-f-l form) tab sch) (get-val (or-f-r form) tab sch))]
      [(not-f? form) (not (get-val (not-f-e form) row sch))]
      [(eq-f? form) (equal? (get-column-value sch (eq-f-name form) row) (eq-f-val form))]
      [(eq2-f? form) (equal? (get-column-value sch (eq2-f-name form) row) (get-column-value sch (eq2-f-name2 form) row))]
      [(lt-f? form) (< (get-column-value sch (lt-f-name form) row) (lt-f-val form))]
      [else (error "error: invalid form")]))
  (table (table-schema tab) (filter (lambda (r) (if (get-val form r (table-schema tab)) #t #f)) (table-rows tab))))

;(table-select (and-f (eq-f 'capital #t) (not-f (lt-f 'area 300))) cities)
  


; Złączenie kartezjańskie

(define (flatten lst)
  (if (empty? lst)
      '()
      (append (first lst) (flatten (rest lst)))))

(define (table-cross-join tab1 tab2)
  (table
   (append (table-schema tab1) (table-schema tab2))
   (flatten (map (lambda (r1)
          (map (lambda (r2) (append r1 r2))
               (table-rows tab2)))
    (table-rows tab1)))))

;(table-cross-join cities (table-rename 'country 'country2 countries))



; Złączenie

(define (convert-table-to-col-names tab)
  (map (lambda (x) (column-info-name x)) (table-schema tab)))

(define (table-natural-join tab1 tab2)
  (define (repeated-cols tab1 tab2)
    (filter (lambda (x) (member x (convert-table-to-col-names tab1))) (convert-table-to-col-names tab2)))

  (define repeated-cols-at-start (repeated-cols tab1 tab2))
  
  (define (change-names tab1 tab2)
    (define rp (repeated-cols tab1 tab2))
    (if (empty? rp)
        tab2
        (change-names tab1 (table-rename (first rp) (cons (first rp) "1") tab2))))

  (define (get-identities name tab)
    (table-select (eq2-f name (cons name "1")) tab))

  (define tcj (table-cross-join tab1 (change-names tab1 tab2)))

  (define (clear-table rpts tab)
    (if (empty? rpts)
        tab
        (clear-table (rest rpts) (table-project (remove (cons (first rpts) "1") (convert-table-to-col-names tcj)) tab))))

  (clear-table repeated-cols-at-start (table (table-schema tcj) (flatten (map (lambda (x) (table-rows (get-identities x tcj))) repeated-cols-at-start)))))
  

;(table-natural-join cities countries)
