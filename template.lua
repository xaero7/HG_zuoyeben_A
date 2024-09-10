function Math(elem)
  -- 如果是行内数学公式，使用 $ 包围
  if elem.mathtype == "InlineMath" then
    return pandoc.RawInline("latex", "$" .. elem.text .. "$")
  end
  -- 如果是显示数学公式，保持不变
  return elem
end

