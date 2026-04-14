$fn=60;
difference() {
  union()  {
    cylinder(d=25+4,h=12.5);
    translate([-11,0,0])cube([20,29/2,12.5]);
    translate([-3,-18,0])cube([6,5,12.5]);
  }
  cylinder(d=25,h=12.5+4);
  translate([-1,-19,0])cube([2,7,13.5]);
  translate([-5,-16,7])rotate([0,90,0])cylinder(d=1,h=10);
}
translate([-11,13,0])cube([20,8,1]);
