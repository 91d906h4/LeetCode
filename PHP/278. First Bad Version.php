<?php
/* The isBadVersion API is defined in the parent class VersionControl.
      public function isBadVersion($version){} */

class Solution extends VersionControl {
    /**
     * @param Integer $n
     * @return Integer
     */
    function firstBadVersion($n) {
        $l = 0;
        $r = $n;
        while($l <= $r){
            $m = round(($l + $r) / 2);
            if($this->isBadVersion($m)) $r = $m - 1;
            else $l = $m + 1;
        }
        return $l;
    }
}
