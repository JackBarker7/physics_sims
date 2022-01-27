function [ r_moon ] = r_moon_42( t )
%Returns the position of the moon for exercise 4.2 (orbiting moon)
    Omega = 2.6615e-6;
    R0 = 222;
    r_moon = R0 * [cos(Omega*t), sin(Omega*t)];
end

