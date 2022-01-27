function [ acceleration ] = a( Rr , Rm )
% Calculates the acceleration of the rocket
% All distances should be in moon radii, and all masses should be in moon
% masses
% Input:
% * Rr: 2-element vector describing the position of the rocket
% * Rm: 2-element vector from the Earth to the moon

% Output:
% * acceleration: the acceleration vecctor

    Me = 83.3;
    G = 9.63e-7;
    acceleration = -G*((Me*Rr/(norm(Rr)^3))+((Rr-Rm)/(norm(Rr-Rm)^3)));
end

