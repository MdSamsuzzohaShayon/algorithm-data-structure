/*
 * YouTube - https://www.youtube.com/watch?v=_dt773ImwFw&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=33
 *
 * Tower of Hanoi
 * The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
 *    Only one dist may be moved at a time
 *    Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod. And lastly
 *    No disk may be placed on top of a disk that is smaller.
 *
 * Shift 'n-1' disks from 'A' to 'B', using 'C' (when required)
 * Shift last disk from 'A' to 'C'
 * Shift 'n-1' disks from 'B' to 'C', using 'A' (when required)
 */


function towerOfHanoi(n, fromRod, toRod, usingRod) {
  if(n === 1){
    console.log(`Move disk 1 from ${fromRod} to ${toRod}`);
    return;
  }

  towerOfHanoi(n-1, fromRod, usingRod, toRod);
  console.log(`Move disk ${n} from ${fromRod} to ${toRod}`);
  towerOfHanoi(n-1, usingRod, toRod, fromRod);
}

towerOfHanoi(2, 'A', 'C', 'B');


// Big-O = O(2^n)
