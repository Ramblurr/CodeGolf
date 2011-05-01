(defn num->digits [n]
  """ Takes a number and returns a sequence containing
      its digits in ascending order
      e.g., 123 -> (1 2 3)"""
 (loop [num n, digits ()] (if (zero? num) (seq digits) (recur (quot num 10) (cons (mod num 10) digits)))))
(defn digits->num [seq]
  """ Takes a sequence of digits and returns the number
      they represent
      e.g., (1 2 3) -> 123 """
  (reduce (fn [a b](+ b (* a 10))) seq))

(defn look-seq [n]
    (digits->num (mapcat (juxt count first) (partition-by identity (num->digits n)))))

(defn look-n-say [n]
  """ Returns a lazy sequence representing
    Conway's look-and-say sequence starting at n """
  (iterate look-seq n))

(println (take 5 (look-n-say 1)))
