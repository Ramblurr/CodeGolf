#!/usr/bin/env clj-env-dir

(defn parse [n]
  (repeatedly n
    #(let [x (read-line)]
      (try
        (doall (parse (Integer/parseInt x)))
        (catch Exception e x)
))))

(defn width [x]
  (reduce max
          (map (fn [%]
            (if (seq? %)
              (+ (width %) 4)
              (count %))
          ) x
  ))
)

(require '[clojure.contrib.string :as s])

(defn out [maxw,n,o]
  (let [b #( let [p (dec o)]
    (println (str (s/repeat p "| ") % (s/repeat (- maxw (* 4 p) 2) "-") % (s/repeat p " |"))))]
    (b \.)
    (doseq [i n]
      (if (seq? i)
        (out maxw i (inc o))
        (println (str (s/repeat o "| ") i (s/repeat (- maxw (count i) (* o 4)) " ") (s/repeat o " |")))
      )
    )
    (b \')
))

(let [root (parse 1)]
    (out (width root) (first root) 1)
)


