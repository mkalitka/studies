#lang racket

(define (cycle! lst)
  (define p lst)
  (define (cycle-helper! lst p)
    (if (null? (mcdr lst))
        (set-mcdr! lst p)
        (cycle-helper! (mcdr lst) p)))
  (cycle-helper! lst p))

(define m (mcons 1 (mcons 2 (mcons 3 null))))
(cycle! m)