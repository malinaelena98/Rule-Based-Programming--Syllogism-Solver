;(defrule citeste_input
;=>
;(assert (premise1 a))
;(assert (premise2 e))
;(assert (conclusion a))
;(assert (tip d)))


(defrule caz1
    (premise1 a)
    (premise2 a)
    (conclusion a)
	(tip 1)
    =>
    (assert (valid))
)
(defrule caz2
    (premise1 e)
    (premise2 a)
    (conclusion e)
	(tip 1)
    =>
    (assert (valid))
)
(defrule caz3
    (premise1 a)
    (premise2 i)
    (conclusion i)
	(tip 1)
    =>
    (assert (valid))
)
(defrule caz4
    (premise1 e)
    (premise2 i)
    (conclusion o)
	(tip 1)
    =>
    (assert (valid))
)
(defrule caz5
    (premise1 e)
    (premise2 a)
    (conclusion e)
	(tip 2)
    =>
    (assert (valid))
)
(defrule caz6
    (premise1 a)
    (premise2 e)
    (conclusion e)
	(tip 2)
    =>
    (assert (valid))
)
(defrule caz7
    (premise1 e)
    (premise2 i)
    (conclusion o)
	(tip 2)
    =>
    (assert (valid))
)
(defrule caz8
    (premise1 a)
    (premise2 o)
    (conclusion o)
	(tip 2)
    =>
    (assert (valid))
)
(defrule caz9
    (premise1 i)
    (premise2 a)
    (conclusion i)
	(tip 3)
    =>
    (assert (valid))
)
(defrule caz10
    (premise1 o)
    (premise2 a)
    (conclusion o)
	(tip 3)
    =>
    (assert (valid))
)
(defrule caz11
    (premise1 a)
    (premise2 i)
    (conclusion i)
	(tip 3)
    =>
    (assert (valid))
)
(defrule caz12
    (premise1 e)
    (premise2 i)
    (conclusion o)
	(tip 3)
    =>
    (assert (valid))
)
(defrule caz13
    (premise1 i)
    (premise2 a)
    (conclusion i)
	(tip 4)
    =>
    (assert (valid))
)
(defrule caz14
    (premise1 a)
    (premise2 e)
    (conclusion e)
	(tip 4)
    =>
    (assert (valid))
)
(defrule caz15
    (premise1 e)
    (premise2 i)
    (conclusion o)
	(tip 4)
    =>
    (assert (valid))
)