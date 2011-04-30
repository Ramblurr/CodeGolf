#!/usr/bin/env clj-env-dir

(defn parse [n]
  (repeatedly n
    #(let [x (read-line)]
      (try
        (doall (#'parse (Integer/parseInt x)))
        (catch Exception e x)
))))
(defn parsen [n,p]
  (apply concat (repeatedly n #(let [x (read-line)]
      (try
        [(parsen (Integer/parseInt x) (str p "| ")) (list (str p "." "" "-"))
]
        (catch Exception e [(list p x " ")])
)))))
(defn flat1 [coll]
  (mapcat #(if (coll? %) % [%]) coll))
(defn parsem [p]
  (let [x (read-line)]
    (try
      (let [n (Integer/parseInt x)]
        [[(str p ".") "| " "-"]
         (doall (repeatedly n #(#'parsem (str p "| "))))
         [(str p "'") "" "-"]
        ]
      )
      (catch Exception e [p x " "])
)))

(defn width [x]
    (println x)
    (map (fn [i] (let [[prefix text fill] i]
       (println i)
        (+(* 2 (count prefix)) (count text)))
    ) x)
)
(defn w [x]
  (reduce max
          (map (fn [%]
            (if (seq? %)
              (+ (#'w %) 4)
              (count %))
          ) x
  ))
)

(require '[clojure.contrib.string :as s])

(defn p_head [o]
  (println (str (s/repeat o "| ") "." (s/repeat (- width (* 4 o) 2) "-") "." (s/repeat o " |")))
)
(defn p_tail [o]
  (println (str (s/repeat o "| ") "'" (s/repeat (- width (* 4 o) 2) "-") "'" (s/repeat o " |")))
)
(defn out [n,o]
  (p_head (dec o))
  (doseq [i n]
    (if (seq? i)
      (#'out i (inc o))
      (println (str (s/repeat o "| ") i (s/repeat (- width (count i) (* o 4)) " ") (s/repeat o " |")))
    )
  )
  (p_tail (dec o))
)
(use 'clojure.contrib.trace)
;(dotrace [parsem] (parsem "" ))
(let [root (parse 1)]
    ;(dotrace [w] (w root))
    ;(println (w root))
    (def width (w root))
;    (dotrace [out] (out root 1))
    (out (first root) 1)

)


