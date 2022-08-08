<?php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function factorial($k){
        $r = 1;
        for($i = 1; $i <= $k; $i++) $r *= $i;
        return $r;
    }
    function uniquePaths($m, $n) {
        return $this->factorial($m + $n - 2) / ($this->factorial($m - 1) * $this->factorial($n - 1));
    }
}
