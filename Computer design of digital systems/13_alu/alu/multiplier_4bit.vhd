library ieee;
use ieee.std_logic_1164.all;

entity multiplier_4bit is 
    port (
        x: in  std_logic_vector (3 downto 0);
        y: in  std_logic_vector (3 downto 0);
        p: out std_logic_vector (7 downto 0)
    );
end entity multiplier_4bit;

architecture multiplier_arch of multiplier_4bit is
component adder_4bit
      Port ( 	a : in STD_LOGIC_VECTOR (3 downto 0);
					b : in STD_LOGIC_VECTOR (3 downto 0);
					cin : in STD_LOGIC;
					sum : out STD_LOGIC_VECTOR (3 downto 0);
					cout : out STD_LOGIC);
end component;
-- AND Product terms:
    signal G0, G1, G2:  std_logic_vector (3 downto 0);
-- B Inputs (B0 has three bits of AND product)
    signal B0, B1, B2:  std_logic_vector (3 downto 0);

begin

    -- y(1) thru y (3) AND products, assigned aggregates:
    G0 <= (x(3) and y(1), x(2) and y(1), x(1) and y(1), x(0) and y(1));
    G1 <= (x(3) and y(2), x(2) and y(2), x(1) and y(2), x(0) and y(2));
    G2 <= (x(3) and y(3), x(2) and y(3), x(1) and y(3), x(0) and y(3));
    -- y(0) AND products (and y0(3) '0'):
    B0 <=  ('0',          x(3) and y(0), x(2) and y(0), x(1) and y(0));

-- named association:
cell_1: 
    adder_4bit 
        port map (
            a => G0,
            b => B0,
            cin => '0',
            cout => B1(3), -- named association can be in any order
            sum(3) => B1(2), -- individual elements of S, all are associated
            sum(2) => B1(1), -- all formal members must be provide contiguously
            sum(1) => B1(0),
            sum(0) => p(1)
        );
cell_2: 
    adder_4bit 
        port map (
            a => G1,
            b => B1,
            cin => '0',
            cout => B2(3),
            sum(3) => B2(2),
            sum(2) => B2(1),
            sum(1) => B2(0),
            sum(0) => p(2)
        );
cell_3: 
    adder_4bit 
        port map (
            a => G2,
            b => B2,
            cin => '0',
            cout => p(7),
            sum => p(6 downto 3)  -- matching elements for formal
        );
    p(0) <= x(0) and y(0); 
end architecture multiplier_arch;