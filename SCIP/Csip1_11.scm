(define (Fn n)
    (cond ((< n 3) n) (+ (Fn (- n 1)) (* 2 (Fn (- n 2))) (* 3 (Fn (- n 3))))))
