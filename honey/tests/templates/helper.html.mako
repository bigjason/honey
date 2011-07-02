<%def name='repeat(s, times)'>
    % for x in range(times):
        ${ 'This is number'.format(x) }
    % endfor
</%def>