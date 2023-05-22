#lang racket

(define (suffixes xs)
  (define (pom ys)
    (if (empty? ys)
        empty
        (cons ys (pom (rest ys)))))
  (pom xs))

; 1 1 0

(define/contract (suffixes/c xs)
  (parametric->/c [a] (-> (listof a) (listof (listof a))))
  (define (pom ys)
    (if (empty? ys)
        '()
        (cons ys (pom (rest ys)))))
  (pom xs))
  
; 241 243 122

(time (suffixes (range 3000)))
;(time (suffixes/c (range 3000)))