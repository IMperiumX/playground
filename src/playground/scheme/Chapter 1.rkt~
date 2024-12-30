#lang sicp

; Exercise 1.2
(/ (+ (+ 5 4) (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 6 2) (- 2 7)))


; Exercise 1.3

(define (square x)
    (* x x))

(define (sum-of-squares x y)
    (+ (square x) (square y)))

(define (largest2-sum-of-squares x y z)
          ;;; x is excluded
    (cond ((and (<= x y) (<= x z)) (sum-of-squares y z))
          ;;; y is excluded
          ((and (<= y x) (<= y z)) (sum-of-squares x z))
          ;;; z is excluded
          ((and (<= z x) (<= z y)) (sum-of-squares x y))))
          ;;; Note: It's also tempting to go for (else (sum-of-squares x y)))

(largest2-sum-of-squares 0 2 1)


