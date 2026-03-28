function play(path)   
    f_path="/usr/local/freeswitch/sounds/slc.xlogix.ca/ivr/arabic_audio/"..path..".wav"
    session:answer();
    session:setAutoHangup(true);
    session:execute("set","ringback=in-ring");
    session:set_tts_params("flite", "kal");
    session:streamFile(f_path);
    session:sleep(100);
end
function nm(c)
      local units = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
      return units[c]
end

function convertnum(number)
    local f = 0

    if number > 999999 then
        local x = math.floor(number / 100000000)
        if x > 0 then
            if x == 1 then
                play("hundred")
            elseif x == 2 then
                play("two_hundred")
            else
                local str_x = nm(x)
                play(str_x)
                play("hundred")
            end

            play("and")
            number = number%100000000
        end

        local x = math.floor(number/1000000)
        local c = x % 10

        if c == 0 then
            if x == 10 then
                play("ten")
            elseif x == 20 then
                play("twenty")
            elseif x == 30 then
                play("thirty")
            elseif x == 40 then
                play("forty")
            elseif x == 50 then
                play("fifty")
            elseif x == 60 then
                play("sixty")
            elseif x == 70 then
                play("seventy")
            elseif x == 80 then
                play("eighty")
            elseif x==90 then
                play("ninety")
            end
        else
            if x < 21 then
                local str_x = nm(x)
                play(str_x)
            elseif x < 30 then
                local str_x = nm(c)
                play(str_x)
                play("twenty")
            elseif x < 40 then
                local str_x = nm(c)
                play(str_x)
                play("thirty")
            elseif x < 50 then
                local str_x = nm(c)
                play(str_x)
                play("forty")
            elseif x < 60 then
                local str_x = nm(c)
                play(str_x)
                play("fifty")
            elseif x < 70 then
                local str_x = nm(c)
                play(str_x)
                play("sixty")
            elseif x < 80 then
                local str_x = nm(c)
                play(str_x)
                play("seventy")
            elseif x < 90 then
                local str_x = nm(c)
                play(str_x)
                play("eighty")
            elseif x < 100 then
                local str_x = nm(c)
                play(str_x)
                play("ninety")
            end
        end

        play("million")
        play("and")
        number = number % 1000000
    end

    if number > 999 then
        local x = math.floor(number / 100000)
        if x > 0 then
            if x == 1 then
                play("hundred")
            elseif x == 2 then
                play("two_hundred")
            else
                local str_x = nm(x)
                play(str_x)
                play("hundred")
            end
            number = number % 100000
        end

        local x = math.floor(number/1000)
        local f = x % 10

        if f == 0 then
            if x == 10 then
                play("ten")
            elseif x == 20 then
                play("twenty")
            elseif x == 30 then
                play("thirty")
            elseif x == 40 then
                play("forty")
            elseif x == 50 then
                play("fifty")
            elseif x == 60 then
                play("sixty")
            elseif x == 70 then
                play("seventy")
            elseif x == 80 then
                play("eighty")
            elseif x == 90 then
                play("ninety")
            end
        else
            if x < 21 then
                local str_x = nm(x)
                play(str_x)
            elseif x < 30 then
                local str_x = nm(f)
                play(str_x)
                play("twenty")
            elseif x < 40 then
                local str_x = nm(f)
                play(str_x)
                play("thirty")
            elseif x < 50 then
                local str_x = nm(f)
                play(str_x)
                play("forty")
            elseif x < 60 then
                local str_x = nm(f)
                play(str_x)
                play("fifty")
            elseif x < 70 then
                local str_x = nm(f)
                play(str_x)
                play("sixty")
            elseif x < 80 then
                local str_x = nm(f)
                play(str_x)
                play("seventy")
            elseif x < 90 then
                local str_x = nm(f)
                play(str_x)
                play("eighty")
            elseif x < 100 then
                local str_x = nm(f)
                play(str_x)
                play("ninety")
            end
        end

        play("thousand")
        play("and")
        number = number % 1000
    end

    if number > 0 then
        local x = math.floor(number / 100)
        if x > 0 then
            if x == 1 then
                play("hundred")
            elseif x == 2 then
                play("two_hundred")
            else
                local str_x = nm(x)
                play(str_x)
                play("hundred")
            end
            number = number % 100
        end

        local x = number
        local j = x % 10

        if j == 0 then
            if x == 10 then
                play("ten")
            elseif x == 20 then
                play("twenty")
            elseif x == 30 then
                play("thirty")
            elseif x == 40 then
                play("forty")
            elseif x == 50 then
                play("fifty")
            elseif x == 60 then
                play("sixty")
            elseif x == 70 then
                play("seventy")
            elseif x == 80 then
                play("eighty")
            elseif x == 90 then
                play("ninety")
            end
        else
            if x < 21 then
                local str_x = nm(x)
                play(str_x)
            elseif x < 30 then
                local str_x = nm(f)
                play(str_x)
                play("twenty")
            elseif x < 40 then
                local str_x = nm(f)
                play(str_x)
                play("thirty")
            elseif x < 50 then
                local str_x = nm(f)
                play(str_x)
                play("forty")
            elseif x < 60 then
                local str_x = nm(f)
                play(str_x)
                play("fifty")
            elseif x < 70 then
                local str_x = nm(f)
                play(str_x)
                play("sixty")
            elseif x < 80 then
                local str_x = nm(f)
                play(str_x)
                play("seventy")
            elseif x < 90 then
                local str_x = nm(f)
                play(str_x)
                play("eighty")
            elseif x < 100 then
                local str_x = nm(f)
                play(str_x)
                play("ninety")
            end
        end
    end
end
convertnum(4121)

