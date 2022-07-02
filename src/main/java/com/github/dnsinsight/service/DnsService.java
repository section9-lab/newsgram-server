package com.github.dnsinsight.service;

import cn.hutool.core.util.RuntimeUtil;
import cn.hutool.core.util.StrUtil;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 10:43
 * @Description:
 */
@Service
public class DnsService {
    public List<String> findDnsInfo(String domain) {
        return RuntimeUtil.execForLines("dig " + domain)
                .stream()
                .filter(StrUtil::isNotBlank)
                .collect(Collectors.toList());
    }
}
