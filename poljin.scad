include <roundedcube.scad>

module poljin() {
  difference(){
    translate([0,-8,0])roundedcube(([50,128,10]),radius=2);
    translate([-7,0,9]) rotate([0,90,0]) roundedcube([7,13,70],radius=3);
    translate([-5,116,4]) rotate([0,90,0]) cylinder(d=5,h=60);
    translate([46,-1,6])rotate([90,0,0])cylinder(d=3,h=10);
  }
}

module teline() {
  difference(){
    translate([0,-8,0])rotate([-15,0,0])
      difference(){
      union(){
	roundedcube([24,23,75],radius=4);
	roundedcube([10,124,43],radius=3);
      }
      translate([-1,6,0])cube([21,10,70]);
      translate([16,11,10])rotate([0,90,0])cylinder(d=8,h=10);
      translate([3,8,72])rotate([90,0,0])cylinder(d=3,h=10);
    }
    translate([-50,-9,-151]) cube(150);
    translate([-5,116,4]) rotate([0,90,0]) cylinder(d=5,h=20);
  }
}

translate([-50,0,0])
poljin();
teline();
