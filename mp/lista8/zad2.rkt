#lang racket

(define (mreverse! lst)
  (define (mreverse-helper! current prev)
    (if (null? current)
        prev
        (let ([next (mcdr current)])
          (set-mcdr! current prev)
          (mreverse-helper! next current))))
  (mreverse-helper! lst '()))

(define m (mcons 1 (mcons 2 (mcons 3 (mcons 4 null)))))
(mreverse! m)