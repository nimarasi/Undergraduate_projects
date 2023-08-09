library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity subtractor_4bit is
Port ( 	a : in STD_LOGIC_VECTOR (3 downto 0);
		b : in STD_LOGIC_VECTOR (3 downto 0);
		bin : in STD_LOGIC;
		diff : out STD_LOGIC_VECTOR (3 downto 0);
		bout : out STD_LOGIC);
end subtractor_4bit;
architecture Behavioral of subtractor_4bit is
component fullsubtractor is
Port(	a : in STD_LOGIC;
		b : in STD_LOGIC;
		bin : in STD_LOGIC;
		diff : out STD_LOGIC;
		bout : out STD_LOGIC);
end component;
signal br0,br1,br2: std_logic;
begin
	fs1: fullsubtractor port map(a(0),b(0),bin,diff(0),br0);
	fs2: fullsubtractor port map(a(1),b(1),br0,diff(1),br1);
	fs3: fullsubtractor port map(a(2),b(2),br1,diff(2),br2);
	fs4: fullsubtractor port map(a(3),b(3),br2,diff(3),bout);
end Behavioral;

