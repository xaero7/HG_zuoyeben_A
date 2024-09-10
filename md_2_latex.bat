pandoc tmp.md -o tmp.tex ^
	--from=markdown ^
	--to=latex ^
	--lua-filter=template.lua
::	--template=template.tex
	