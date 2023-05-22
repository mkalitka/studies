#lang racket

(require rackunit)

(define (proc x y z)
  (cond [(and (>= x z) (>= y z)) (+ (* x x) (* y y))]
        [(and (>= y x) (>= z x)) (+ (* y y) (* z z))]
        [else (+ (* x x) (* z z))]))

(check-equal? (proc 16 3 75) 5881)
(check-equal? (proc 3 4 4) 32)
(check-true (number? (proc 0 0 0)))
(check-true (number? (proc -1 -3 -2)))

(proc 16 8 8)