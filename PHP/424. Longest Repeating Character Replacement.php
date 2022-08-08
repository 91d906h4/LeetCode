<?php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function characterReplacement($s, $k) {
        $m = $r = 0;
        for($i = 0; $i < strlen($s); $i++){
            $t[$s[$i]] += 1;
            $m = max($m, $t[$s[$i]]);
            if($r - $m < $k) $r += 1;
            else $t[$s[$i - $r]] -= 1;
        }
        return $r;
    }
}
