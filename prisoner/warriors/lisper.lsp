; The Little Lisper
; By Arrdem
; http://codegolf.stackexchange.com/questions/2357/1p5-iterated-prisoners-dilemma/2373#2373
(setf *r* 0.0)
(setf *s* 0.0)
(setf *k* 0.0)
(setf *e* 0.0)

;; step 1 - cout up all the games results

(loop for i from 1 to (length(car *args*)) do
    (setf foo (char (car *args*) (1- i)))
    (cond
        ((equal foo #\R) (setf *r* (1+ *r*)))
        ((equal foo #\S) (setf *s* (1+ *s*)))
        ((equal foo #\K) (setf *k* (1+ *k*)))
        ((equal foo #\E) (setf *e* (1+ *e*)))
    )
)

(setf *sum* (+ *r* *s* *k* *e*))

;; step 2 - rate trustworthiness
(if (> *sum* 0)
    (progn
        (setf *dbag* (/ (+ *r* *e*) *sum*)) ; percentage chance he rats
        (setf *trust* (/ (+ *s* *k*) *sum*)); percentage chance he clams
    )
    (progn
        (setf *dbag* 0) ; percentage chance he rats
        (setf *trust* 0); percentage chance he clams
    )
)



;; step 3 - make a decision (the hard part....)

(write-char
    (cond
        ((or (= *dbag* 1) (= *trust* 1)) #\t) ; maximizes both cases
                                              ; takes advantage of the angel, crockblocks the devil
        ((> *dbag* *trust*) #\t)              ; crockblock statistical jerks
        ((< *dbag* *trust*) #\c)              ; reward the trusting (WARN - BACKSTABBING WOULD IMPROVE SCORE)
        ((and
            (= (floor *dbag* 0.1) (floor *trust* 0.1))
            (not (= 0 *dbag* *trust*)))
            #\t)                              ; try to backstab a purely random opponent, avoid opening w/ a backstab
        (t #\c)                               ; defalt case - altruism
    )
)