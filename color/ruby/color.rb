
#Calculate a complement color from a supplied 24bit color.
#Copyright 2022. thomas.cherry@gmail.com

def as_color(colors, text)
  red = colors[0]
  green = colors[1]
  blue = colors[2]
  return f"\033[38;2;{red};{green};{blue}m{text}\033[00m"
end

def expand_color

def find_compliment(colors)
  return [255-colors[0], 255-colors[1], 255-colors[2]]
end

def ask_for_number(which)
  value = -1
  while value<0 or value>255 do
    puts ("enter a number for #{which}")
    value = Integer(gets)
  end
  return value
end

def ask_for_color()
  red = ask_for_number("red")
  green = ask_for_number("green")
  blue = ask_for_number("blue")
  return [red, green, blue]
end

def main()
  color = ask_for_color()
  compliment = find_compliment(color)
  puts (compliment)
end

main()