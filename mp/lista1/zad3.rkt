#lang racket

(* (+ 2 2) 5) ;działa

(* (+ 2 2) (5) ) ;nie działa

(*(+(2 2) 5) ) ;nie działa

(*(+ 2
     2) 5) ;działa

(5 * 4) ;nie działa

(5 * (2 + 2) ) ;nie działa

((+ 2 3) ) ;nie działa

+ ;działa

( define + (* 2 3) ) ;działa

+ ;działa

(* 2 +) ;działa

( define ( five ) 5) ;działa

( define four 4) ;działa

(five) ;działa

four ;działa

five ;działa

(four) ;nie działa