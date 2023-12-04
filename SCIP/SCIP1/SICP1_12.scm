(define (pascal row col)
    (cond ((> col row)      999)
          ((or (= row col)  (= col 0))   1)
          (else             (+ (pascal (- row 1) (- col 1)) (pascal (- row 1) col)))))


(define (f2p row col)
    (/ (factorial row) (* (factorial col) (factorial (- row col)))))

(define (fib n)
    (fib-iter 1 0 n))

(define (fib-iter a b count)
    (if (= count 0)
        b  
        (fib-iter (+ a b) a (- count 1))))

(define (factorial n)
    (fact-iter 1 1 n))

(define (fact-iter product counter max-count)
    (if (> counter max-count)
        product
        (fact-iter (* counter product)
                   (+ counter 1)
                   max-count)))