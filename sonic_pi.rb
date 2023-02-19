live_loop :foo do
  use_real_time
  use_synth :piano
  a, b, c = sync "/osc*/trigger/piano"
  play chord(a, b), sustain: c
end

live_loop :notes do
  use_real_time
  use_synth :piano
  d = sync "/osc*/user"
  play d
end