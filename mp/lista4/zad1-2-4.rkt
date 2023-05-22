#lang racket

(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

(define (fold-tree f base t)
  (if (leaf? t)
      base
      (f (fold-tree f base (node-l t))
         (node-elem t)
         (fold-tree f base (node-r t)))))

(define (tree-sum t)
  (fold-tree + 0 t))

(define t
  (node
   (node (leaf) 2 (leaf))
   5
   (node (node (leaf) 6 (leaf))
         8
         (node (leaf) 9 (leaf)))))

(define (tree-flip t)
  (define (swap l m r) (node r m l))
  (fold-tree swap (leaf) t))

(define (tree-height t)
  (define (max-height l m r)
    (+ (max l r) 1))
  (fold-tree max-height 0 t))

(define (tree-span t)
  (define (bst-pair l m r)
    (cond [(and (null? l) (null? r) (cons m m))]
      [(null? l) (m (cdr r))]
      [(null? r) ((car l) m)]
      [else (cons (car l) (cdr r))]))
  (fold-tree bst-pair null t))

(define (flatten t)
  (define (join-list l m r)
    (append l (list m) r))
  (fold-tree join-list null t))

(flatten t)