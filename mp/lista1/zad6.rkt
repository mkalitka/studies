#lang racket

(define ifCond (< 2 3))
(define ifTrue "true")
(define ifFalse "false")

(define (ifFunction ifCond ifTrue ifFalse)
  (or (and ifCond ifTrue) ifFalse))

(ifFunction ifCond ifTrue ifFalse)