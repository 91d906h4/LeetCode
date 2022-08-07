<?php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function fib($n) {
        $fib = array(0, 1);
        for($i = 2; $i <= $n; $i++){
            $fib[$i] = $fib[$i - 1] + $fib[$i - 2];
        }
        return $fib[$n];
    }
}
