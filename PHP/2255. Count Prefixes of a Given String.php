class Solution {

    /**
     * @param String[] $words
     * @param String $s
     * @return Integer
     */
    function countPrefixes($words, $s) {
        $counter = 0;
        for($i = 0;$i < count($words);$i++){
            if(str_starts_with($s, $words[$i])) $counter++;
        }
        return $counter;
    }
}
