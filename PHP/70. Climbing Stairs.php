<?php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function climbStairs($n) {
        $t = array(1, 1);
        for($i = 2; $i <= $n; $i++){
            $t[$i] = $t[$i - 1] + $t[$i - 2];
        }
        return $t[$n];
    }
}
