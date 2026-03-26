include <roundedcube.scad>
$fn=60;

module topseli() {
  difference(){
    hull() {
      cylinder(d=18,h=15);
      translate([(46-18)/2,1,0])cylinder(d=20,h=15);
      translate([46-18,0,0])cylinder(d=18,h=15);
    }
    translate([10/10,1,0]) cylinder(d=5.5,h=18);
    translate([46-18-0.8,1,0])cylinder(d=5.5,h=18);
    translate([(46-18)/2,2,0])cylinder(d=5.5,h=18);
  }
}




width=100;
length=73;
height=36;
radius=7;
thick=3;
lid_height=6;
lip_height=5;

module box () {
difference(){
  roundedcube([width,length,height],radius=radius);
  translate([thick,thick,thick])
  roundedcube([width-2*thick,length-2*thick,height-2*thick],radius=radius-thick);
  translate([0,0,height-lid_height]) cube([width,length,lid_height+1]);
  translate([90,21,17])rotate([0,90,0])cylinder(d=12,h=10);
  translate([0,67,10])rotate([0,90,0])cylinder(d=6,h=10);
 }
}
module lid() {
  difference(){ union(){
      difference(){
	roundedcube([width,length,lid_height+radius],radius=radius);
	translate([0,0,lid_height]) cube([width,length,lid_height+5]);
      }
      difference(){
	translate([thick+0.3,thick+0.3,thick])
	  roundedcube([width-(2*thick)-0.6,length-2*thick-0.6,lid_height+lip_height+radius],radius=radius-thick);
	translate([0,0,lid_height+lip_height]) cube([width,length,lid_height+radius+3]);
      }
    }
    translate([2*thick,2*thick,thick])
      roundedcube([width-4*thick,length-4*thick,lid_height+lip_height+radius],radius=radius-2*thick);
  }
}


module reikia() {
  for (i=[10:10:width-10]){
    translate([i,0,11]) rotate([-90,0,0]) cylinder(d=5,h=length+10);
  }
  for (i=[10:10:width-10]){
    translate([i,0,20]) rotate([-90,0,0]) cylinder(d=5,h=length+10);
  }
}

translate([0,length+3,0])lid();
difference(){  box();reikia(); }


translate([47,14,-15])topseli();

