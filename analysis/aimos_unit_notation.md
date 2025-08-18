b:bent, e:extended
p:proximal_tilted, d:distal_tilted

45>p->sonic35(4b)>d->pass23>dp-

# 個人用メモ
## props
- 回転方向 (rotation dir)
	- 正 (positive)
	- 負 (negative)
- 移動方向 (displacement dir)
	- 昇り (rised)
	- 降り (fallen)

- 動作方向 (movement)
	- 拡大 (widen)
	- 縮小 (narrow)

- 内余指 (inner_finger)
	- bent
	- extented

- tilt
	- y_tilt
		- p傾 (p_tilted)
		- d傾 (d_tilted)
	- x_tilt
		- u傾 (u_tilted)
		- r傾 (r_tilted)


## tricks lists
### Planar Fingerswitch
#### Pass (Pe)
##### Applicable Props
There are 8 basic variations of pass.
1. rotation dir
2. x-tilt
3. displacement

##### Basic Variations
ex. 2-4 passes

`p- > pass34:23 > p-`
`p+ > pass34:23 > p+`
`d- > pass34:23 > d-`
`d+ > pass34:23 > d+`
`p- > pass23:34 > p-`
`p+ > pass23:34 > p+`
`d- > pass23:34 > d-`
`d+ > pass23:34 > d+`
	2. Flush pass (Pf)
		- Props
			1. rotation dir
			2. tilt
			3. movement
		- Basic Variations
			ex. 2-5 flush passes
				34 > p- > flush_pass:25(3b4e) > p-
				34 > p+ > flush_pass:25(4b3e) > p+
				34 > d- > flush_pass:25(4b3e) > d-
				34 > d+ > flush_pass:25(3b4e) > d+
				25(3b4e) > p+ > flush_pass:34 > p+
				25(4b3e) > p- > flush_pass:34 > p-
				25(4b3e) > d+ > flush_pass:34 > d+
				25(3b4e) > d- > flush_pass:34 > d-
2. Conical Fingerswitch
	1. Sonic
		- Props
	    1. rotation dir = tilt
			2. movement
			3. displacement
			4. inner finger
	  - Symmetrical Affix
      1. mir
      2. inv
      3. ant
      4. rev
		- Basic Variations
			ex. 2-4 sonics
				34 > p- > sonic:24(3b) > d-
        23 > p+ > sonic:24(3b) > d+
				34 > d- > sonic:24(3e) > p-
				23 > d+ > sonic:24(3e) > p+
				34 > d+ > sonic:24(3b) > p+
				23 > d- > sonic:24(3b) > p-
				34 > p+ > sonic:24(3e) > d+
				23 > p- > sonic:24(3e) > d-
        24(3b) > d+ > sonic:34 > p+
        23(3b) > d- > sonic:23 > p-
        24(3e) > p+ > sonic:34 > d+
        23(3e) > p- > sonic:23 > d-
        24(3b) > p- > sonic:34 > d-
        23(3b) > p+ > sonic:23 > d+
        24(3e) > d- > sonic:34 > p-
        23(3e) > d+ > sonic:23 > p+
  2. East Sonic
    - Props
    - Symmetrical Affix
      1. mir
      2. inv
      3. ant = mir&inv
      4. rev
      Aside from "antipodal", the other 3 are independent.
		- Basic Variations
      ex. 2-5 east sonics
        45 > p- > east_sonic:23 > d-
        23 > p+ > east_sonic:45 > d+
        45 > d- > east_sonic:23 > p-
        45 > d+ > east_sonic:23 > p+
        23 > d- > east_sonic:45 > p-
        23 > d+ > east_sonic:45 > p+
        45 > p+ > east_sonic:23 > d+
        23 > p- > east_sonic:45 > d-
	2. Flush Sonic
		- Props
    - Symmetrical Affix
      1. mir
      2. inv
      3. ant = mir&inv
      4. rev
      Aside from "antipodal", the other 3 are independent.
		- Basic Variations
			ex. 2-5 flush sonics
	      34 > p- > flush_sonic:25(3b4e) > d-
	      34 > p+ > flush_sonic:25(4b3e) > d+
				34 > d- > flush_sonic:24(4b3e) > p-
				34 > d+ > flush_sonic:24(3b4e) > p+
        25(3b4e) > p+ > flush_sonic:34 > d+
        25(4b3e) > p- > flush_sonic:34 > d-
				24(4b3e) > d+ > flush_sonic:34 > p+
				24(3b4e) > d- > flush_sonic:34 > p-




mir=[-,+,+]
inv=[]
ant
rev=[-,+,-]



rot+,tilt+,mov+
(+++)
(-++)
(+-+)
(--+)
(++-)
(-+-)
(+--)
(---)