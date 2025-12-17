% This file is part of the project's source code.
% Copyright (c) 2025 Daniel Monzon.
% Licensed under the MIT License. See the LICENSE file in the repository root.

function Req = parallel_resistance(R_values)
%PARALLEL_RESISTANCE Computes equivalent resistance of resistors in parallel.
%   Req = PARALLEL_RESISTANCE(R_values) returns the equivalent resistance Req
%   of any number of resistors connected in parallel.
%
%   INPUT:
%       R_values : Vector containing the resistance values in ohms.
%                  It can be a row or column vector, e.g. [100 220 330].
%
%   OUTPUT:
%       Req      : Equivalent resistance in ohms.
%
%   The formula used is:
%       1/Req = sum(1/R_i)  for i = 1..n

    % Check if the input is provided
    if nargin < 1
        error('At least one input argument (R_values) is required.');
    end

    % Validate that R_values is numeric
    if ~isnumeric(R_values)
        error('Input R_values must be numeric.');
    end

    % Validate that R_values is a vector
    if ~isvector(R_values)
        error('Input R_values must be a vector.');
    end

    % Validate that all resistance values are positive and non-zero
    if any(R_values <= 0)
        error('All resistance values must be positive and non-zero.');
    end

    % Compute the sum of reciprocals of the resistances
    reciprocal_sum = sum(1 ./ R_values);

    % Avoid division by zero in case of unexpected numerical issues
    if reciprocal_sum == 0
        error('The sum of reciprocals is zero, cannot compute equivalent resistance.');
    end

    % Compute the equivalent resistance
    Req = 1 / reciprocal_sum;
end

