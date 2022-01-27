function [ tout , pos ] = simulate_rocket ( init_pos , init_vel , moon_pos , t )
% Simulate the rocket trajectory with the Earth and Moon influence. The coordinate
% used in this function is centred at Earth’s centre (i.e. Earth centre at (0,0) )
% and scaled in Moon−radius.
% The simulation finishes when it simulates for the whole t, or the rocket landed
% on the Moon.
% Input:
% * init_pos: 2−elements vector (x, y) indicating the initial position of the rocket.
% * init_vel: 2−elements vector (vx, vy) of the initial velocity of the rocket.
% * moon_pos: a function that receives time, t, and return a 2−elements vector (x, y)
% (see hint) indicating the Moon position relative to Earth.
% * t: an N−elements vector of the time step where the position of the rocket will be
% returned.
%
% Output:
% * tout: an M−elements vector of the time step where the position is described,
% if the rocket does not land on the Moon, M = N.
% * pos: (M x 2) matrix indicating the positions of the rocket as function of time,
% with the first column is x and the second column is y.

    Rr = init_pos; %variable holding position of rocket
    Vr = init_vel; %variable holding velocity of rocket
    
    dt = t(2)-t(1); %calculate time step from first 2 values in t array
       
    tout = t; %initialise the tout variable. We can take a slice of this later if the simulation finishes early
    pos = zeros(length(t), 2); %initialise array to hold positions
    
    for i = 1:length(t)
        
        Rm = moon_pos(t(i)); %get moon position
        
        Rr_prime = Rr + dt*Vr; %get new x' and y'

        Vr_prime = Vr + dt/2 * (a(Rr, Rm) + a(Rr_prime, Rm)); %get new vx' and vy'
        
        Rr = Rr + dt/2 * (Vr+Vr_prime); %get new x and y
        
        Vr = Vr_prime; %get new vx and vy
        
        pos(i, :) = Rr;
        
        if norm(Rr-Rm)<1
            %if rocket has reached the moon, break out of the loop
            %we also need to slice the relevant arrays
            
            tout = t(1:i);
            pos = pos(1:i, :);
            break
        end
    end
end

