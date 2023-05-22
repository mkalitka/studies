#lang racket

(define (suffixes xs)
  (if (null? xs) '(()) (cons xs (suffixes (cdr xs)))))

(define (sorted? xs)
  (cond [(null? xs) #t]
        [(null? (cdr xs)) #t]
        [(> (car xs) (cadr xs)) #f]
        [else (sorted? (cdr xs))]))

(sorted? '(1 2 3 4 4 4 5 6 7))