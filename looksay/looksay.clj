(def z `~(count ""))
(def ten (read-string (str z "xa")))
(defn num->digits [n]
  " Takes a number and returns a sequence containing
    its digits in ascending order
    e.g., 123 -> (1 2 3)"
 (loop [num n, digits ()] (if (zero? num) (seq digits) (recur (quot num ten) (cons (mod num ten) digits)))))
(defn digits->num [seq]
  " Takes a sequence of digits and returns the number
    they represent
    e.g., (1 2 3) -> 123 "
  (reduce (fn [a b](+ b (* a ten))) seq))

(defn look-seq [n]
  " Returns a sequence containing the look-say representation for n"
    (digits->num (mapcat (juxt count first) (partition-by identity (num->digits n)))))

(defn look-n-say
  " Returns a lazy sequence representing
    Conway's look-and-say sequence starting at n"
  ([] (look-n-say (inc z)))
  ([n] (iterate look-seq n)))

(println (take (+ ten ten) (look-n-say)))
