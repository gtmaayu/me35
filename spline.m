clear; clc; 

wayPoints = [0 0; 2 2; ... 
    -6 -16 ; 0 -12; ... 
    7 -16; -2 6; ... 
    -4 4; -2 2; ... 
    0 0]; % XY loc of each waypoint

ts = 0.2; % time in s between each waypoint
posDiv = 10; % number of intervals on each segment in ms
height = size(wayPoints);
height = height(1); % number of waypoints 
timeLength = ts * height; % time from first to last waypoint
t = linspace(0,timeLength,4*posDiv); % time array 

x2 = wayPoints([3:5],1); 
y2 = wayPoints([3:5],2); 

xx2 = linspace(x2(1),x2(3),posDiv)
yy2 = spline(x2,y2,xx2)

data = [xx2; yy2];

data = array2table(data)
writetable(data,'armData1.csv','Delimiter',',','QuoteStrings',true);
type 'armData.csv';

% plotting all of the 
figure 
hold on 
plot(xx2,yy2); 
hold off​
